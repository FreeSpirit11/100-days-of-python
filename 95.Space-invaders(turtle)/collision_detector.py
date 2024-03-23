import time

class CollisionDetector:
    def bullet_bunker(self, bunker, alien):
        """
        Detect collision of alien bullets with bunkers.

        Args:
        - bunker: Bunker object
        - alien: Alien object

        This method checks for collisions between alien bullets and bunker segments.
        If a collision is detected, it removes the bullet, bunker segment, and updates
        the game state accordingly.
        """
        for bullet in alien.bullets:
            for segment in bunker.segments:
                if bullet.distance(segment) < 30 and segment.xcor() - 3 < bullet.xcor() < segment.xcor() + 3:
                    bullet.clear()
                    bullet.hideturtle()
                    segment.clear()
                    segment.hideturtle()
                    bunker.segments.remove(segment)
                    alien.bullets.remove(bullet)
                    break

    def laser_bunker(self, shooter, bunker):
        """
        Detect collision of laser with bunkers.

        Args:
        - shooter: Shooter object
        - bunker: Bunker object

        This method checks for collisions between the shooter's lasers and bunker segments.
        If a collision is detected, it removes the laser, bunker segment, and updates
        the game state accordingly.
        """
        for laser in shooter.lasers:
            for segment in bunker.segments:
                if laser.distance(segment) < 33 and segment.xcor() - 3 < laser.xcor() < segment.xcor() + 3:
                    laser.clear()
                    laser.hideturtle()
                    segment.clear()
                    segment.hideturtle()
                    shooter.lasers.remove(laser)
                    bunker.segments.remove(segment)
                    break

    def laser_alien(self, shooter, alien):
        """
        Detect collision of laser with aliens.

        Args:
        - shooter: Shooter object
        - alien: Alien object

        This method checks for collisions between the shooter's lasers and alien spaceships.
        If a collision is detected, it removes the laser, alien spaceship, and updates
        the game state accordingly. Returns True if a collision is detected, else False.
        """
        for laser in shooter.lasers:
            for alien_spaceship in alien.aliens:
                if laser.distance(
                        alien_spaceship) < 20 and alien_spaceship.xcor() - 10 < laser.xcor() < alien_spaceship.xcor() + 10:
                    laser.clear()
                    laser.hideturtle()
                    alien_spaceship.clear()
                    alien_spaceship.hideturtle()
                    shooter.lasers.remove(laser)
                    alien.aliens.remove(alien_spaceship)
                    return True
        return False

    def laser_bullet(self, shooter, alien):
        """
        Detect collision of laser with alien bullets.

        Args:
        - shooter: Shooter object
        - alien: Alien object

        This method checks for collisions between the shooter's lasers and alien bullets.
        If a collision is detected, it removes the laser, alien bullet, and updates
        the game state accordingly.
        """
        for laser in shooter.lasers:
            for bullet in alien.bullets:
                if laser.distance(bullet) < 33 and bullet.xcor() - 3 < laser.xcor() < bullet.xcor() + 3:
                    laser.clear()
                    laser.hideturtle()
                    bullet.clear()
                    bullet.hideturtle()
                    shooter.lasers.remove(laser)
                    alien.bullets.remove(bullet)
                    break

    def bullet_shooter(self, alien, shooter):
        """
        Detect collision of bullet with shooter.

        Args:
        - alien: Alien object
        - shooter: Shooter object

        This method checks for collisions between alien bullets and the shooter.
        If a collision is detected, it removes the shooter, bullet, and updates
        the game state accordingly. Returns the removed shooter object if a collision
        is detected, else returns False.
        """
        try:
            shooter1 = shooter.shooters[0]
            # Detect collision of bullet with shooter
            for bullet in alien.bullets:
                if shooter1.distance(bullet) < 30 and shooter1.xcor() - 20 < bullet.xcor() < shooter1.xcor() + 20:
                    shooter1.clear()
                    shooter1.hideturtle()
                    bullet.clear()
                    bullet.hideturtle()
                    shooter.shooters.remove(shooter1)
                    alien.bullets.remove(bullet)
                    time.sleep(2)  # Pause the game for 2 seconds
                    shooter.get_helper_shooter()
                    return shooter1
        except IndexError:
            return False
        return True
