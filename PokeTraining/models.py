from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import date


# Create your models here.
class Pokemon(models.Model):
    ALL_NATURES = (
        ('HARDY', 'Hardy'),
        ('LONELY', 'Lonely'),
        ('BRAVE', 'Brave'),
        ('ADAMANT', 'Adamant'),
        ('NAUGHTY', 'Naughty'),
        ('BOLD', 'Bold'),
        ('DOCILE', 'Docile'),
        ('RELAXED', 'Relaxed'),
        ('IMPISH', 'Impish'),
        ('LAX', 'Lax'),
        ('TIMID', 'Timid'),
        ('HASTY', 'Hasty'),
        ('SERIOUS', 'Serious'),
        ('JOLLY', 'Jolly'),
        ('NAIVE', 'Naive'),
        ('MODEST', 'Modest'),
        ('MILD', 'Mild'),
        ('QUIET', 'Quiet'),
        ('BASHFUL', 'Bashful'),
        ('RASH', 'Rash'),
        ('CALM', 'Calm'),
        ('GENTLE', 'Gentle'),
        ('SASSY', 'Sassy'),
        ('CAREFUL', 'Careful'),
        ('QUIRKY', 'Quirky')
    )

    ALL_GENERATIONS = (
        ('1', 'Kanto'),
        ('2', 'Johto'),
        ('3', 'Hoenn'),
        ('4', 'Sinnoh'),
        ('5', 'Unova'),
        ('6', 'Kalos'),
        ('7', 'Alola'),
        ('8', 'Galar')
    )

    ALL_BALLS = (
        ('POKE', 'Pokeball'),
        ('GREAT', 'Great Ball'),
        ('ULTRA', 'Ultra Ball'),
        ('MASTER', 'Master Ball'),
        ('DIVE', 'Dive Ball'),
        ('FAST', 'Fast Ball'),
        ('BEAST', 'Beast Ball'),
        ('DUSK', 'Dusk Ball'),
        ('HEAL', 'Heal Ball'),
        ('LEVEL', 'Level Ball'),
        ('LOVE', 'Love Ball'),
        ('FRIEND', 'Friend Ball'),
        ('NEST', 'Nest Ball'),
        ('LUXURY', 'Luxury Ball'),
        ('HEAVY', 'Heavy Ball'),
        ('NET', 'Net Ball'),
        ('MOON', 'Moon Ball'),
        ('LURE', 'Lure Ball'),
        ('QUICK', 'Quick Ball'),
        ('PREMIER', 'Premier Ball'),
        ('TIMER', 'Timer Ball'),
        ('REPEAT', 'Repeat Ball')
    )

    ALL_TYPES = (
        ('NORMAL', 'Normal'),
        ('FIRE', 'Fire'),
        ('FIGHTING', 'Fighting'),
        ('WATER', 'Water'),
        ('FLYING', 'Flying'),
        ('GRASS', 'Grass'),
        ('POISON', 'Poison'),
        ('ELECTRIC', 'Electric'),
        ('GROUND', 'Ground'),
        ('PSYCHIC', 'Psychic'),
        ('ROCK', 'Rock'),
        ('ICE', 'Ice'),
        ('BUG', 'Bug'),
        ('DRAGON', 'Dragon'),
        ('GHOST', 'Ghost'),
        ('DARK', 'Dark'),
        ('STEEL', 'Steel'),
        ('FAIRY', 'Fairy')
    )

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('G', 'Genderless')
    )

    pkmn_name = models.CharField(max_length=40, default='Pikachu')
    pkmn_nickname = models.CharField(max_length=40, default='')
    pkmn_number = models.PositiveIntegerField(default=1, null=True)
    pkmn_level = models.PositiveIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    pkmn_type1 = models.CharField(max_length=40,
                                  choices=ALL_TYPES,
                                  default='NORMAL')
    pkmn_type2 = models.CharField(max_length=40,
                                  choices=ALL_TYPES,
                                  null=True)
    pkmn_gender = models.CharField(max_length=11,
                                   choices=GENDERS,
                                   default='G')
    ball_captured = models.CharField(max_length=40,
                                     choices=ALL_BALLS,
                                     default='POKE')
    original_generation = models.CharField(max_length=40,
                                           choices=ALL_GENERATIONS,
                                           default='7')
    held_item = models.CharField(max_length=40, null=True)
    ability = models.CharField(max_length=40)
    nature = models.CharField(max_length=40,
                              choices=ALL_NATURES,
                              default='ADAMANT')
    pkrs = models.BooleanField(default=False)
    shiny = models.BooleanField(default=False)
    captured_date = models.DateField(default=date.today)
    ev_trained = models.BooleanField(default=False)

    def __str__(self):
        return self.pkmn_name


class Attacks(models.Model):
    attacks = models.OneToOneField(Pokemon,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    attack1 = models.CharField(max_length=40, default='Toxic')
    attack2 = models.CharField(max_length=40, default='Hidden Power')
    attack3 = models.CharField(max_length=40, default='Double Team')
    attack4 = models.CharField(max_length=40, default='Hyper Beam')

    def __str__(self):
        return "Attack 1: %s\n" \
               "Attack 2: %s\n" \
               "Attack 3: %s\n" \
               "Attack 4: %s" \
               % (self.attack1,
                  self.attack2,
                  self.attack3,
                  self.attack4)


class Stats(models.Model):
    stats = models.OneToOneField(Pokemon,
                                 on_delete=models.CASCADE,
                                 primary_key=True)

    ev_hp = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(512)
    ])
    ev_atk = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(512)
    ])
    ev_def = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(512)
    ])
    ev_satk = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(512)
    ])
    ev_sdef = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(512)
    ])
    ev_spd = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(512)
    ])

    iv_hp = models.PositiveIntegerField(default=31, validators=[
        MinValueValidator(0),
        MaxValueValidator(31)
    ])
    iv_atk = models.PositiveIntegerField(default=31, validators=[
        MinValueValidator(0),
        MaxValueValidator(31)
    ])
    iv_def = models.PositiveIntegerField(default=31, validators=[
        MinValueValidator(0),
        MaxValueValidator(31)
    ])
    iv_satk = models.PositiveIntegerField(default=31, validators=[
        MinValueValidator(0),
        MaxValueValidator(31)
    ])
    iv_sdef = models.PositiveIntegerField(default=31, validators=[
        MinValueValidator(0),
        MaxValueValidator(31)
    ])
    iv_spd = models.PositiveIntegerField(default=31, validators=[
        MinValueValidator(0),
        MaxValueValidator(31)
    ])

    def __str__(self):
        return self.ev_hp


class OriginalTrainer(models.Model):
    ot = models.OneToOneField(Pokemon,
                              on_delete=models.CASCADE,
                              primary_key=True)
    pkmn_ot = models.CharField(max_length=15, default='Jonathon')
    trainer_id = models.PositiveIntegerField(default=857172, validators=[
        MinValueValidator(0),
        MaxValueValidator(999999)
    ])

    def __str__(self):
        return "Pokemon Trainer: %s\n" \
               "Trainer ID: %s" % (self.pkmn_ot, self.trainer_id)