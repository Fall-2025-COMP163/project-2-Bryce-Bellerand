"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Bryce Bellerand
Date: 11-5-2025

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""
# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

import random

class Character:
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        damage = random.randint(1, self.strength)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} took {damage} damage! Remaining health: {self.health}")

    def display_stats(self):
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")

class Player(Character):
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | Experience: {self.experience}")

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 20, 5)

    def attack(self, target):
        damage = random.randint(5, self.strength + 5)
        print(f"{self.name} swings mightily for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        power_damage = random.randint(15, self.strength + 15)
        print(f"{self.name} performs a POWER STRIKE for {power_damage} damage!")
        target.take_damage(power_damage)

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        damage = random.randint(5, self.magic)
        print(f"{self.name} casts a spell for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        damage = random.randint(10, self.magic + 10)
        print(f"{self.name} hurls a FIREBALL for {damage} damage!")
        target.take_damage(damage)

class Rogue(Player):
    def __init__(self, name):
        self.magic_usage = False
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        if self.magic_usage == False:
            damage = random.randint(1, self.strength) 
            if random.randint(1, 10) <= 3:
                damage *= 4
                print("💥 Critical hit!")
            print(f"{self.name} strikes for {damage} damage!")
            target.take_damage(damage)
        elif self.magic_usage == True:
            damage = random.randint(1, (self.magic + self.strength)//2) 
            if random.randint(1, 10) <= 3:
                damage *= 4
                print("💥 Critical hit!")
            print(f"{self.name} attacks for {damage} damage!")
            target.take_damage(damage)

    def sneak_attack(self, target):
        if self.magic_usage == True:
            damage = (random.randint(1, (self.magic + self.strength)//2)) * 4
            print(f"{self.name} performs a SNEAK ATTACK for {damage} damage!")
            target.take_damage(damage)
        else:
            damage = (random.randint(1, self.strength)) * 4
            print(f"{self.name} performs a SNEAK ATTACK for {damage} damage!")
            target.take_damage(damage)

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # TODO: Store weapon name and damage bonus
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    magic_rouge = Rogue("Shadow")
    magic_rouge.magic_usage = True

    # TODO: Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    magic_rouge.display_stats()

    # TODO: Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
     
    for character in [warrior, mage, rogue, magic_rouge]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    target4 = Character("Enemy4", 50, 0, 0)
    # 
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    magic_rouge.sneak_attack(target4)
    
    # TODO: Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    # 
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # TODO: Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
