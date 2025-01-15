import math, random

## Double octothorpes are important comments
# Single hashes are the developers thoughts

class player():
    def __init__(self,health,speed,damage,crit,name):
        ## Name of player, duh
        self.name = name
        ## Health is input as a range of 75-250 upon creation of a player
        self.health = health
        ## Speed is measured on a scale of 1-10; It approximately equals the chance out of 10 to hit
        self.speed = speed
        self.tempSpeed = speed
        # I just realized I made AC from D&D
        ## Damage has a range of 7-21
        self.damage = damage
        ## Crit has a range of 5%-22%
        ## Crits, by default, multiply damage for one hit by 1.5 times
        self.crit = crit
        ## Stores current hit on [x] player
        self.tempHit = 0

    def attack(self,target):
        self.speed = self.tempSpeed
        ran = random.random()
        if self.crit > ran:
            self.tempHit = self.damage * 1.5
        else:
            self.tempHit = self.damage
        x = getattr(target, 'health')
        x -= self.tempHit
        return x

    def can_hit(self,speed): ## Percent chance for one player to it the other
        ran = round(random.random(),2)
        spIs = round(speed/self.speed,2)
        return spIs > ran

    def is_alive(self):
        return self.health > 0

    def disengage(self):
        self.speed *= 3