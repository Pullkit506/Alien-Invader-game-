
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import sys
import pygame
from bullets import Bullet, Missile, Torpedo
from alien import Alien
from pygame.sprite import Group
from pygame.sprite import Sprite

from random import randint
import random
from time import sleep

# we don't need to import settings, ship classes because we already did it in main class remeber when you use sum function of python standard library we dont need to import library into PSL


def check_keyDown(settings, screen, event, ship, bullet, missiles, stats, button, aliens, torpedo, bullets):
    if event.key == pygame.K_RIGHT:
        ship.right = True
    elif event.key == pygame.K_LEFT:
        ship.left = True
    elif event.key == pygame.K_UP:
        ship.up = True
    elif event.key == pygame.K_DOWN:
        ship.down = True
    elif event.key == pygame.K_SPACE and not settings.empty_bullet:
        # create new bullets and add to bullet group
        new_bullet = Bullet(screen, settings, ship)
        bullet.add(new_bullet)
    elif event.key == pygame.K_r and not settings.empty_missiles:
        new_missile = Missile(screen, settings, ship)
        missiles.add(new_missile)

    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        screen_rect = screen.get_rect()
        mouse_x, mouse_y = screen_rect.center
        check_play_button(stats, button, mouse_x, mouse_y, aliens,
                          torpedo, missiles, bullets, ship, screen, settings)


def check_keyUp(event, ship, bullet):
    if event.key == pygame.K_RIGHT:
        ship.right = False
    elif event.key == pygame.K_LEFT:
        ship.left = False
    elif event.key == pygame.K_UP:
        ship.up = False
    elif event.key == pygame.K_DOWN:
        ship.down = False


def check_play_button(stats, button, mouse_x, mouse_y, aliens, torpedo, missiles, bullets, ship, screen, settings):
    if button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.reset_stat()
        stats.game_active = True
        settings.reset_settings()

        pygame.mouse.set_visible(False)

    # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        missiles.empty()
        torpedo.empty()

    # create new fleet
        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()


def check_events(settings, screen, ship, bullet, missiles, stats, button, torpedo, aliens):
    # responding to game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # keydown tells when a key is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # which returns a tuple containing the x- and y-coordinates of the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, button, mouse_x, mouse_y, aliens,
                              torpedo, missiles, bullet, ship, screen, settings)
        elif event.type == pygame.KEYDOWN:
            check_keyDown(settings, screen, event, ship, bullet,
                          missiles, stats, button, aliens, torpedo, bullet)

        # keyUp function tells when a key is releases
        elif event.type == pygame.KEYUP:
            check_keyUp(event, ship, bullet)


def update_screen(ai_settings, screen, ship, bg_img, bullet, missiles, aliens, torpedo, button, stats, sb):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.

    # screen.fill(ai_settings.bg_color)

    # pygame.display.flip() will continually update the display to show the new positions of elements and hide the old ones, creating the illusion of smooth movement.

    # adding image of ship and background to game
    ai_settings.blitscreen(screen, bg_img)
    # blit - copy the contents of one Surface onto another Surface

    # Redraw all bullets before we call flip
    for bullet in bullet.sprites():
        bullet.draw_bullets()

    for missile in missiles.sprites():
        missile.draw_missiles()

    for torpedo in torpedo.sprites():
        torpedo.draw_torpedo()
    # When you call draw() on a group, Pygame automatically draws each ele- ment in the group at the position defined by its rect attribute.
    aliens.draw(screen)
    sb.draw_score()

    # for alien in aliens.sprites():
    #     alien.draw_aliens()

    ship.blitme()
    # before flip but after all other images so that button appears on top
    if not stats.game_active:
        button.draw_button()
    # make most recently drawn screen visible
    pygame.display.flip()


def check_bullet_alien_collision(bullets, aliens, missiles, stats, settings, sb):
    collisions1 = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions2 = pygame.sprite.groupcollide(missiles, aliens, False, True)
    # The two True arguments tell Pygame whether to delete the bullets and aliens that have collided. (To make a high-powered bullet that’s able to travel to the top of the screen, destroying every alien in its path, you could set the first Boolean argument to False and keep the second Boolean argument set to True.

    # collisions  is dictionary
    if collisions1 or collisions2:
        # values in the collisions dictionary. Remember that each value is a list of aliens hit by a single bullet. We multiply the value of each alien by the number of aliens in each list and add this amount to the current score.
        for aliens in collisions2.values():
            stats.score += settings.points*len(aliens) - 20
            sb.prep_score()
        for aliens in collisions1.values():
            stats.score += settings.points
            sb.prep_score()


def update_rid(bullets, missiles, settings, aliens, SHIP, screen, torpedo, bg_img, stats, sb):

    bullets.update()
    missiles.update()
    torpedo.update()
   # You shouldn’t remove items from a list or group within a for loop, so
    # we have to loop over a copy of the group
    check_bullet_alien_collision(
        bullets, aliens, missiles, stats, settings, sb)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()

        missiles.empty()
        torpedo.empty()
        while settings.level_counter < 3:
            settings.level_counter += 1
            settings.blitscreen(screen, bg_img)
            pygame.display.flip()
            sleep(1)
            break
        create_fleet(settings, screen, aliens, SHIP)

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            settings.Total_bullets = settings.Total_bullets - 1
            if (settings.Total_bullets == 0):
                settings.empty_bullet = True

    for missile in missiles.copy():
        if missile.rect.bottom <= 0:
            missiles.remove(missile)
            settings.Total_missiles = settings.Total_missiles - 1

            if (settings.Total_missiles == 0):
                settings.empty_missiles = True

    for torped in torpedo.copy():
        if torped.rect.bottom >= settings.length:
            torpedo.remove(torped)


def create_fleet(ai_settings, screen, aliens, ship):
    # this function helps in creating fleet of aliens only
    # Spacing between each alien is equal to one alien width

    # We need to know the alien’s width and height in order to place aliens, so we create an alien atu before we perform calculations. This alien won’t be part of the fleet, so don’t add it to the group aliens.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width  # inbuilt width function
    available_SpaceX = ai_settings.width - 2*alien_width
    number_of_ship = available_SpaceX/(2*alien_width - 10)

    # y
    available_SpaceY = (ai_settings.length -
                        (3 * alien.rect.height) - (ship.rect.height))
    number_rows = available_SpaceY/(2*alien.rect.height)

    if ai_settings.level_counter == 1:
        for j in range(int(number_rows)):
            for i in range(int(number_of_ship)):
                alien = Alien(ai_settings, screen)
                alien.rect.x = alien_width + 2*i*alien_width
                alien.rect.y = alien.rect.height + 2*j*alien.rect.height
                aliens.add(alien)
    elif ai_settings.level_counter == 2:
        ai_settings.points = 75
        for i in range(1, int(number_rows)+2):
            n = 0
            m = 0
            for j in range(0, i):
                alien = Alien(ai_settings, screen)
                alien.rect.x = alien_width + 2*j*alien_width
                alien.rect.y = alien.rect.height + (i-1)*alien.rect.height
                aliens.add(alien)
                n = j+1
            for k in range(n, 2*(int(number_rows)+1-i)+1+n):
                if i == 4:
                    alien = Alien(ai_settings, screen)
                    alien.rect.x = alien_width + 2*k*alien_width
                    alien.rect.y = alien.rect.height + (i-1)*alien.rect.height
                    aliens.add(alien)

                m = k+1

            for l in range(m, m+i):
                alien = Alien(ai_settings, screen)
                alien.rect.x = alien_width + 2*l*alien_width
                alien.rect.y = alien.rect.height + (i-1)*alien.rect.height
                aliens.add(alien)

        for i in reversed(range(1, int(number_rows)+2)):
            n = 0
            m = 0
            for j in range(0, i):
                alien = Alien(ai_settings, screen)
                alien.rect.x = alien_width + 2*j*alien_width
                alien.rect.y = (alien.rect.height +
                                ((int(number_rows)+5 - i)*alien.rect.height))
                aliens.add(alien)
                n = j+1
            for k in range(n, 2*(int(number_rows)+1-i)+1+n):
                if i == 4:
                    alien = Alien(ai_settings, screen)
                    alien.rect.x = alien_width + 2*k*alien_width
                    alien.rect.y = (alien.rect.height +
                                    ((int(number_rows)+5 - i)*alien.rect.height))
                    aliens.add(alien)
                m = k+1

            for l in range(m, m+i):
                alien = Alien(ai_settings, screen)
                alien.rect.x = alien_width + 2*l*alien_width
                alien.rect.y = (alien.rect.height +
                                ((int(number_rows)+5 - i)*alien.rect.height))
                aliens.add(alien)


def drop_down(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y = alien.rect.y + ai_settings.fleet_drop_speed

    ai_settings.fleet_direction = -1*ai_settings.fleet_direction


def ship_hit(ai_settings, aliens, ship, stats, screen, bullets, missiles, torpedo, button):
    if stats.ship_left > 0:
        stats.ship_left = stats.ship_left-1

        aliens.empty()
        bullets.empty()
        missiles.empty()
        torpedo.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, bullets, aliens, ship, stats, missiles, torpedo, button):

    drop_down(ai_settings, aliens)
    aliens.update()

    # The method spritecollideany() takes two arguments: a sprite and a group. The method looks for any member of the group that’s collided with the sprite and stops looping through the group as soon as it finds one mem- ber that has collided with the sprite.
    check_alien_bottom(ai_settings, stats, screen, ship,
                       aliens, bullets, missiles, torpedo)

    if pygame.sprite.spritecollideany(ship, aliens, collided=pygame.sprite.collide_rect_ratio(0.6)) or pygame.sprite.spritecollideany(ship, torpedo, collided=pygame.sprite.collide_rect_ratio(0.6)):
        ship_hit(ai_settings, aliens, ship, stats,
                 screen, bullets, missiles, torpedo, button)

        # The sprite.groupcollide() method compares each bullet’s rect with each alien’s rect and returns a dictionary containing the bullets and aliens that have collided. Each key in the dictionary is a bullet, and the corresponding value is the alien that was hit.


def create_torpedo(random_alien, settings, screen, torpedo):
    torped = Torpedo(screen, settings, random_alien)
    torpedo.add(torped)


def torpedo_create(aliens, settings, screen, torpedo, ship):
    mylist = list(aliens)
    alien = random.choice(mylist)

    random_alien = Alien(settings, screen)
    random_alien.rect.x = alien.rect.x
    random_alien.rect.y = alien.rect.y
    create_torpedo(random_alien, settings, screen, torpedo)


def check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets, missiles, torpedo):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, aliens, ship, stats,
                     screen, bullets, missiles, torpedo)
