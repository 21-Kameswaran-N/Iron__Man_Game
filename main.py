import random
import sys

import pygame
from pygame import mixer
from pygame.locals import *

clock = pygame.time.Clock()
# Intialize the pygame
pygame.init()

info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()
screen_width, screen_height = info.current_w, info.current_h

(width, height) = screen_width - 384, screen_height - 272

# create the screen
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Background
background = [pygame.image.load('main.jpg').convert(), pygame.image.load('ironman lead.jpg').convert(),
              pygame.image.load('thanos lead.jpg').convert(), pygame.image.load('game_intro.jpg').convert(),
              pygame.image.load('pause.jpg').convert(), pygame.image.load('help_pg.png').convert()]

# player
# stand
stand = [pygame.image.load('1stand.png').convert_alpha(), pygame.image.load('2stand.png').convert_alpha(),
         pygame.image.load('3stand.png').convert_alpha(),
         pygame.image.load('4stand.png').convert_alpha(), pygame.image.load('5stand.png').convert_alpha(),
         pygame.image.load('6stand.png').convert_alpha(),
         pygame.image.load('7stand.png').convert_alpha(), pygame.image.load('8stand.png').convert_alpha(),
         pygame.image.load('9stand.png').convert_alpha(),
         pygame.image.load('10stand.png').convert_alpha(), pygame.image.load('11stand.png').convert_alpha()]

revstand = [pygame.transform.flip(pygame.image.load('1stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('2stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('3stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('4stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('5stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('6stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('7stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('8stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('9stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('10stand.png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('11stand.png').convert_alpha(), True, False)]

walk = [pygame.image.load('1walk.png').convert_alpha(), pygame.image.load('2walk.png').convert_alpha(),
        pygame.image.load('3walk.png').convert_alpha(),
        pygame.image.load('4walk.png').convert_alpha(), pygame.image.load('5walk.png').convert_alpha(),
        pygame.image.load('6walk.png').convert_alpha(),
        pygame.image.load('7walk.png').convert_alpha(), pygame.image.load('8walk.png').convert_alpha(),
        pygame.image.load('9walk.png').convert_alpha(),
        pygame.image.load('10walk.png').convert_alpha(), pygame.image.load('11walk.png').convert_alpha(),
        pygame.image.load('12walk.png').convert_alpha()]

rev = [pygame.transform.flip(pygame.image.load('1walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('2walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('3walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('4walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('5walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('6walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('7walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('8walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('9walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('10walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('11walk.png').convert_alpha(), True, False),
       pygame.transform.flip(pygame.image.load('12walk.png').convert_alpha(), True, False)]

rfly = [pygame.image.load('1fly.png').convert_alpha(), pygame.image.load('2fly.png').convert_alpha(),
        pygame.image.load('3fly.png').convert_alpha(),
        pygame.image.load('4fly.png').convert_alpha()]

lfly = [pygame.transform.flip(pygame.image.load('1fly.png').convert_alpha(), True, False),
        pygame.transform.flip(pygame.image.load('2fly.png').convert_alpha(), True, False),
        pygame.transform.flip(pygame.image.load('3fly.png').convert_alpha(), True, False),
        pygame.transform.flip(pygame.image.load('4fly.png').convert_alpha(), True, False)]

down = [pygame.image.load('1down.png').convert_alpha(), pygame.image.load('2down.png').convert_alpha(),
        pygame.image.load('3down.png').convert_alpha(),
        pygame.image.load('4down.png').convert_alpha(), pygame.image.load('5down.png').convert_alpha(),
        pygame.image.load('6down.png').convert_alpha(),
        pygame.image.load('7down.png').convert_alpha(), pygame.image.load('8down.png').convert_alpha()]

revdown = [pygame.transform.flip(pygame.image.load('1down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('2down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('3down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('4down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('5down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('6down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('7down.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('8down.png').convert_alpha(), True, False)]

domo = [pygame.image.load('1domo.png').convert_alpha(), pygame.image.load('2domo.png').convert_alpha(),
        pygame.image.load('3domo.png').convert_alpha(),
        pygame.image.load('4domo.png').convert_alpha(), pygame.image.load('5domo.png').convert_alpha(),
        pygame.image.load('6domo.png').convert_alpha(),
        pygame.image.load('7domo.png').convert_alpha(), pygame.image.load('8domo.png').convert_alpha(),
        pygame.image.load('9domo.png').convert_alpha(),
        pygame.image.load('10domo.png').convert_alpha()]

revdomo = [pygame.transform.flip(pygame.image.load('1domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('2domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('3domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('4domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('5domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('6domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('7domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('8domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('9domo.png').convert_alpha(), True, False),
           pygame.transform.flip(pygame.image.load('10domo.png').convert_alpha(), True, False)]

shield = [pygame.image.load('1shield.png').convert_alpha(), pygame.image.load('2shield.png').convert_alpha(),
          pygame.image.load('3shield.png').convert_alpha(),
          pygame.image.load('4shield.png').convert_alpha(), pygame.image.load('5shield.png').convert_alpha(),
          pygame.image.load('6shield.png').convert_alpha(),
          pygame.image.load('7shield.png').convert_alpha(), pygame.image.load('8shield.png').convert_alpha(),
          pygame.image.load('9shield.png').convert_alpha()]

fin_shield = [pygame.image.load('10shield.png').convert_alpha(), pygame.image.load('11shield.png').convert_alpha(),
              pygame.image.load('12shield.png').convert_alpha()]

rev_fin_shield = [pygame.transform.flip(pygame.image.load('10shield.png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('11shield.png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('12shield.png').convert_alpha(), True, False)]

rev_shield = [pygame.transform.flip(pygame.image.load('1shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('2shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('3shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('4shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('5shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('6shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('7shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('8shield.png').convert_alpha(), True, False),
              pygame.transform.flip(pygame.image.load('9shield.png').convert_alpha(), True, False)]

down_shield = [pygame.image.load('1dshield.png').convert_alpha(), pygame.image.load('2dshield.png').convert_alpha(),
               pygame.image.load('3dshield.png').convert_alpha(), pygame.image.load('4dshield.png').convert_alpha(),
               pygame.image.load('5dshield.png').convert_alpha(),
               pygame.image.load('6dshield.png').convert_alpha(), pygame.image.load('7dshield.png').convert_alpha(),
               pygame.image.load('8dshield.png').convert_alpha(),
               pygame.image.load('9dshield.png').convert_alpha(), pygame.image.load('10dshield.png').convert_alpha(),
               pygame.image.load('11dshield.png').convert_alpha()]

fin_down_shield = [pygame.image.load('12dshield.png').convert_alpha(),
                   pygame.image.load('13dshield.png').convert_alpha(),
                   pygame.image.load('14dshield.png').convert_alpha(),
                   pygame.image.load('15dshield.png').convert_alpha()]

rev_down_shield = [pygame.transform.flip(pygame.image.load('1dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('2dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('3dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('4dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('5dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('6dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('7dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('8dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('9dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('10dshield.png').convert_alpha(), True, False),
                   pygame.transform.flip(pygame.image.load('11dshield.png').convert_alpha(), True, False)]

rev_fin_down_shield = [pygame.transform.flip(pygame.image.load('12dshield.png').convert_alpha(), True, False),
                       pygame.transform.flip(pygame.image.load('13dshield.png').convert_alpha(), True, False),
                       pygame.transform.flip(pygame.image.load('14dshield.png').convert_alpha(), True, False),
                       pygame.transform.flip(pygame.image.load('15dshield.png').convert_alpha(), True, False)]

fight = [pygame.image.load('hit 0.png').convert_alpha(), pygame.image.load('hit 1.png').convert_alpha(),
         pygame.image.load('hit 2.png').convert_alpha(),
         pygame.image.load('hit 3.png').convert_alpha(), pygame.image.load('hit 4.png').convert_alpha(),
         pygame.image.load('hit 5.png').convert_alpha(),
         pygame.image.load('hit 6.png').convert_alpha(), pygame.image.load('hit 7.png').convert_alpha(),
         pygame.image.load('hit 8.png').convert_alpha(),
         pygame.image.load('hit 9.png').convert_alpha(), pygame.image.load('hit 10.png').convert_alpha(),
         pygame.image.load('hit 11.png').convert_alpha(),
         pygame.image.load('h_shot 1.png').convert_alpha(),
         pygame.image.load('h_shot 2.png').convert_alpha(), pygame.image.load('h_shot 3.png').convert_alpha(),
         pygame.image.load('h_shot 4.png').convert_alpha(), pygame.image.load('h_shot 5.png').convert_alpha(),
         pygame.image.load('h_shot 6.png').convert_alpha(),
         pygame.image.load('h_shot 7.png').convert_alpha(), pygame.image.load('h_shot 8.png').convert_alpha(),
         pygame.image.load('h_shot 9.png').convert_alpha(),
         pygame.image.load('h_shot 10.png').convert_alpha(), pygame.image.load('h_shot 11.png').convert_alpha(),
         pygame.image.load('h_shot 12.png').convert_alpha(),
         pygame.image.load('s_kick 1.png').convert_alpha(), pygame.image.load('s_kick 2.png').convert_alpha(),
         pygame.image.load('s_kick 3.png').convert_alpha(),
         pygame.image.load('s_kick 4.png').convert_alpha(), pygame.image.load('s_kick 5.png').convert_alpha(),
         pygame.image.load('s_kick 6.png').convert_alpha(),
         pygame.image.load('s_kick 7.png').convert_alpha(), pygame.image.load('s_kick 8.png').convert_alpha(),
         pygame.image.load('s_kick 9.png').convert_alpha(),
         pygame.image.load('s_kick 10.png').convert_alpha(), pygame.image.load('s_kick 11.png').convert_alpha(),
         pygame.image.load('s_kick 12.png').convert_alpha(),
         pygame.image.load('u_kick 1.png').convert_alpha(), pygame.image.load('u_kick 2.png').convert_alpha(),
         pygame.image.load('u_kick 3.png').convert_alpha(),
         pygame.image.load('u_kick 4.png').convert_alpha(), pygame.image.load('u_kick 5.png').convert_alpha(),
         pygame.image.load('u_kick 6.png').convert_alpha(),
         pygame.image.load('u_kick 7.png').convert_alpha(), pygame.image.load('u_kick 8.png').convert_alpha(),
         pygame.image.load('u_kick 9.png').convert_alpha(),
         pygame.image.load('u_kick 10.png').convert_alpha(), pygame.image.load('u_kick 11.png').convert_alpha(),
         pygame.image.load('u_kick 12.png').convert_alpha(),
         pygame.image.load('iron-chk-1.png').convert_alpha(), pygame.image.load('iron-chk-2.png').convert_alpha(),
         pygame.image.load('iron-chk-3.png').convert_alpha(),
         pygame.image.load('iron-chk-4.png').convert_alpha(), pygame.image.load('iron-chk-5.png').convert_alpha(),
         pygame.image.load('iron-chk-6.png').convert_alpha(),
         pygame.image.load('iron-chk-7.png').convert_alpha(), pygame.image.load('iron-chk-8.png').convert_alpha(),
         pygame.image.load('iron-chk-9.png').convert_alpha(),
         pygame.image.load('iron-chk-10.png').convert_alpha(), pygame.image.load('iron-chk-11.png').convert_alpha(),
         pygame.image.load('iron-chk-12.png').convert_alpha(), pygame.image.load('down_hit_1.png').convert_alpha(),
         pygame.image.load('down_hit_2.png').convert_alpha(),
         pygame.image.load('down_hit_3.png').convert_alpha(),
         pygame.image.load('down_hit_4.png').convert_alpha(), pygame.image.load('down_hit_5.png').convert_alpha(),
         pygame.image.load('down_hit_6.png').convert_alpha(),
         pygame.image.load('down_hit_7.png').convert_alpha(), pygame.image.load('down_hit_8.png').convert_alpha(),
         pygame.image.load('down_hit_9.png').convert_alpha(),
         pygame.image.load('down_hit_10.png').convert_alpha(), pygame.image.load('down_hit_11.png').convert_alpha(),
         pygame.image.load('down_hit_12.png').convert_alpha(),
         pygame.image.load('down_shot_1.png').convert_alpha(), pygame.image.load('down_shot_2.png').convert_alpha(),
         pygame.image.load('down_shot_3.png').convert_alpha(),
         pygame.image.load('down_shot_4.png').convert_alpha(), pygame.image.load('down_shot_5.png').convert_alpha(),
         pygame.image.load('down_shot_6.png').convert_alpha(),
         pygame.image.load('down_shot_7.png').convert_alpha(), pygame.image.load('down_shot_8.png').convert_alpha(),
         pygame.image.load('down_shot_9.png').convert_alpha(),
         pygame.image.load('down_shot_10.png').convert_alpha(), pygame.image.load('down_shot_11.png').convert_alpha(),
         pygame.image.load('down_shot_12.png').convert_alpha()]

rev_fight = [pygame.transform.flip(pygame.image.load('hit 0.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('hit 11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('h_shot 12.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('s_kick 12.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('u_kick 12.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('iron-chk-12.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_hit_12.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_1.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_2.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_3.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_4.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_5.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_6.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_7.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_8.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_9.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_10.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_11.png').convert_alpha(), True, False),
             pygame.transform.flip(pygame.image.load('down_shot_12.png').convert_alpha(), True, False)]

chest_beam = [pygame.image.load('chest_beam(1).png').convert_alpha(),
              pygame.image.load('chest_beam(2).png').convert_alpha(),
              pygame.image.load('chest_beam(3).png').convert_alpha(),
              pygame.image.load('chest_beam(4).png').convert_alpha(),
              pygame.image.load('chest_beam(5).png').convert_alpha(),
              pygame.image.load('chest_beam(6).png').convert_alpha(),
              pygame.image.load('chest_beam(7).png').convert_alpha(),
              pygame.image.load('chest_beam(8).png').convert_alpha(),
              pygame.image.load('chest_beam(9).png').convert_alpha(),
              pygame.image.load('chest_beam(10).png').convert_alpha(),
              pygame.image.load('chest_beam(11).png').convert_alpha(),
              pygame.image.load('chest_beam(12).png').convert_alpha(),
              pygame.image.load('chest_beam(13).png').convert_alpha(),
              pygame.image.load('chest_beam(14).png').convert_alpha(),
              pygame.image.load('chest_beam(15).png').convert_alpha(),
              pygame.image.load('chest_beam(16).png').convert_alpha(),
              pygame.image.load('chest_beam(17).png').convert_alpha(),
              pygame.image.load('chest_beam(18).png').convert_alpha(),
              pygame.image.load('chest_beam(19).png').convert_alpha(),
              pygame.image.load('chest_beam(20).png').convert_alpha(),
              pygame.image.load('chest_beam(21).png').convert_alpha(),
              pygame.image.load('chest_beam(22).png').convert_alpha(),
              pygame.image.load('chest_beam(23).png').convert_alpha(),
              pygame.image.load('chest_beam(24).png').convert_alpha(),
              pygame.image.load('chest_beam(25).png').convert_alpha(),
              pygame.image.load('chest_beam(26).png').convert_alpha(),
              pygame.image.load('chest_beam(27).png').convert_alpha(),
              pygame.image.load('chest_beam(28).png').convert_alpha(),
              pygame.image.load('chest_beam(29).png').convert_alpha(),
              pygame.image.load('chest_beam(30).png').convert_alpha(),
              pygame.image.load('chest_beam(31).png').convert_alpha(),
              pygame.image.load('chest_beam(32).png').convert_alpha(),
              pygame.image.load('chest_beam(33).png').convert_alpha(),
              pygame.image.load('chest_beam(34).png').convert_alpha(),
              pygame.image.load('chest_beam(35).png').convert_alpha(),
              pygame.image.load('chest_beam(36).png').convert_alpha(),
              pygame.image.load('chest_beam(37).png').convert_alpha(),
              pygame.image.load('chest_beam(38).png').convert_alpha(),
              pygame.image.load('chest_beam(39).png').convert_alpha(),
              pygame.image.load('chest_beam(40).png').convert_alpha(),
              pygame.image.load('chest_beam(41).png').convert_alpha(),
              pygame.image.load('chest_beam(42).png').convert_alpha(),
              pygame.image.load('chest_beam(43).png').convert_alpha(),
              pygame.image.load('chest_beam(44).png').convert_alpha(),
              pygame.image.load('chest_beam(45).png').convert_alpha(),
              pygame.image.load('chest_beam(46).png').convert_alpha(),
              pygame.image.load('chest_beam(47).png').convert_alpha(),
              pygame.image.load('chest_beam(48).png').convert_alpha(),
              pygame.image.load('chest_beam(49).png').convert_alpha(),
              pygame.image.load('chest_beam(50).png').convert_alpha(),
              pygame.image.load('chest_beam(51).png').convert_alpha()]

rev_chest_beam = [pygame.transform.flip(pygame.image.load('chest_beam(1).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(2).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(3).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(4).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(5).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(6).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(7).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(8).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(9).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(10).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(11).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(12).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(13).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(14).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(15).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(16).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(17).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(18).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(19).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(20).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(21).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(22).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(23).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(24).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(25).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(26).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(27).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(28).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(29).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(30).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(31).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(32).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(33).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(34).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(35).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(36).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(37).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(38).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(39).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(40).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(41).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(42).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(43).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(44).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(45).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(46).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(47).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(48).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(49).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(50).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('chest_beam(51).png').convert_alpha(), True, False)]

ironman_win = [pygame.image.load('ironman win (1).png').convert_alpha(),
               pygame.image.load('ironman win (2).png').convert_alpha(),
               pygame.image.load('ironman win (3).png').convert_alpha(),
               pygame.image.load('ironman win (4).png').convert_alpha(),
               pygame.image.load('ironman win (5).png').convert_alpha(),
               pygame.image.load('ironman win (6).png').convert_alpha(),
               pygame.image.load('ironman win (7).png').convert_alpha(),
               pygame.image.load('ironman win (8).png').convert_alpha(),
               pygame.image.load('ironman win (9).png').convert_alpha(),
               pygame.image.load('ironman win (10).png').convert_alpha(),
               pygame.image.load('ironman win (11).png').convert_alpha(),
               pygame.image.load('ironman win (12).png').convert_alpha(),
               pygame.image.load('ironman win (13).png').convert_alpha(),
               pygame.image.load('ironman win (14).png').convert_alpha(),
               pygame.image.load('ironman win (15).png').convert_alpha(),
               pygame.image.load('ironman win (16).png').convert_alpha(),
               pygame.image.load('ironman win (17).png').convert_alpha(),
               pygame.image.load('ironman win (18).png').convert_alpha(),
               pygame.image.load('ironman win (19).png').convert_alpha(),
               pygame.image.load('ironman win (20).png').convert_alpha(),
               pygame.image.load('ironman win (21).png').convert_alpha(),
               pygame.image.load('ironman win (22).png').convert_alpha()]

dead = [pygame.image.load('defeat (1).png').convert_alpha(),
        pygame.image.load('defeat (2).png').convert_alpha(),
        pygame.image.load('defeat (3).png').convert_alpha(),
        pygame.image.load('defeat (4).png').convert_alpha(),
        pygame.image.load('defeat (5).png').convert_alpha(),
        pygame.image.load('defeat (6).png').convert_alpha(),
        pygame.image.load('defeat (7).png').convert_alpha(),
        pygame.image.load('defeat (8).png').convert_alpha(),
        pygame.image.load('defeat (9).png').convert_alpha(),
        pygame.image.load('defeat (10).png').convert_alpha(),
        pygame.image.load('defeat (11).png').convert_alpha(),
        pygame.image.load('defeat (12).png').convert_alpha(),
        pygame.image.load('defeat (13).png').convert_alpha(),
        pygame.image.load('defeat (14).png').convert_alpha(),
        pygame.image.load('defeat (15).png').convert_alpha(),
        pygame.image.load('defeat (16).png').convert_alpha(),
        pygame.image.load('defeat (17).png').convert_alpha(),
        pygame.image.load('defeat (18).png').convert_alpha(),
        pygame.image.load('defeat (19).png').convert_alpha()]

jarvis = pygame.image.load('jarvis_help.png').convert_alpha()

# enemy
enemy_right_stand = [pygame.image.load('stand (1).png').convert_alpha(),
                     pygame.image.load('stand (2).png').convert_alpha(),
                     pygame.image.load('stand (3).png').convert_alpha(),
                     pygame.image.load('stand (4).png').convert_alpha(),
                     pygame.image.load('stand (5).png').convert_alpha(),
                     pygame.image.load('stand (6).png').convert_alpha(),
                     pygame.image.load('stand (7).png').convert_alpha(),
                     pygame.image.load('stand (8).png').convert_alpha(),
                     pygame.image.load('stand (9).png').convert_alpha(),
                     pygame.image.load('stand (10).png').convert_alpha(),
                     pygame.image.load('stand (11).png').convert_alpha(),
                     pygame.image.load('stand (12).png').convert_alpha(),
                     pygame.image.load('stand (13).png').convert_alpha(),
                     pygame.image.load('stand (14).png').convert_alpha(),
                     pygame.image.load('stand (15).png').convert_alpha(),
                     pygame.image.load('stand (16).png').convert_alpha(),
                     pygame.image.load('stand (17).png').convert_alpha(),
                     pygame.image.load('stand (18).png').convert_alpha(),
                     pygame.image.load('stand (19).png').convert_alpha(),
                     pygame.image.load('stand (20).png').convert_alpha(),
                     pygame.image.load('stand (21).png').convert_alpha(),
                     pygame.image.load('stand (22).png').convert_alpha(),
                     pygame.image.load('stand (23).png').convert_alpha(),
                     pygame.image.load('stand (24).png').convert_alpha(),
                     pygame.image.load('stand (25).png').convert_alpha(),
                     pygame.image.load('stand (26).png').convert_alpha()]

enemy_left_stand = [pygame.transform.flip(pygame.image.load('stand (1).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (2).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (3).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (4).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (5).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (6).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (7).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (8).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (9).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (10).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (11).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (12).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (13).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (14).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (15).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (16).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (17).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (18).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (19).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (20).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (21).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (22).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (23).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (24).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (25).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('stand (26).png').convert_alpha(), True, False)]

enemy_right_walk = [pygame.image.load('right walk (1).png').convert_alpha(),
                    pygame.image.load('right walk (2).png').convert_alpha(),
                    pygame.image.load('right walk (3).png').convert_alpha(),
                    pygame.image.load('right walk (4).png').convert_alpha(),
                    pygame.image.load('right walk (5).png').convert_alpha(),
                    pygame.image.load('right walk (6).png').convert_alpha(),
                    pygame.image.load('right walk (7).png').convert_alpha(),
                    pygame.image.load('right walk (8).png').convert_alpha(),
                    pygame.image.load('right walk (9).png').convert_alpha()]

enemy_left_walk = [pygame.image.load('left walk (1).png').convert_alpha(),
                   pygame.image.load('left walk (2).png').convert_alpha(),
                   pygame.image.load('left walk (3).png').convert_alpha(),
                   pygame.image.load('left walk (4).png').convert_alpha(),
                   pygame.image.load('left walk (5).png').convert_alpha(),
                   pygame.image.load('left walk (6).png').convert_alpha(),
                   pygame.image.load('left walk (7).png').convert_alpha(),
                   pygame.image.load('left walk (8).png').convert_alpha(),
                   pygame.image.load('left walk (9).png').convert_alpha()]

teleport_left = [pygame.image.load('teleport (1).png').convert_alpha(),
                 pygame.image.load('teleport (2).png').convert_alpha(),
                 pygame.image.load('teleport (3).png').convert_alpha(),
                 pygame.image.load('teleport (4).png').convert_alpha(),
                 pygame.image.load('teleport (5).png').convert_alpha(),
                 pygame.image.load('teleport (6).png').convert_alpha(),
                 pygame.image.load('teleport (7).png').convert_alpha(),
                 pygame.image.load('teleport (8).png').convert_alpha(),
                 pygame.image.load('teleport (9).png').convert_alpha(),
                 pygame.image.load('teleport (10).png').convert_alpha()]

teleport_right = [pygame.transform.flip(pygame.image.load('teleport (1).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (2).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (3).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (4).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (5).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (6).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (7).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (8).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (9).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('teleport (10).png').convert_alpha(), True, False)]

enemy_right_hit = [pygame.image.load('hit (1).png').convert_alpha(), pygame.image.load('hit (2).png').convert_alpha(),
                   pygame.image.load('hit (3).png').convert_alpha(), pygame.image.load('hit (4).png').convert_alpha(),
                   pygame.image.load('hit (5).png').convert_alpha(), pygame.image.load('hit (6).png').convert_alpha(),
                   pygame.image.load('hit (7).png').convert_alpha(), pygame.image.load('hit (8).png').convert_alpha(),
                   pygame.image.load('hit (9).png').convert_alpha(), pygame.image.load('hit (10).png').convert_alpha(),
                   pygame.image.load('hit (11).png').convert_alpha(), pygame.image.load('hit (12).png').convert_alpha(),
                   pygame.image.load('hit (13).png').convert_alpha(), pygame.image.load('hit (14).png').convert_alpha(),
                   pygame.image.load('hit (15).png').convert_alpha()]

enemy_left_hit = [pygame.transform.flip(pygame.image.load('hit (1).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (2).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (3).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (4).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (5).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (6).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (7).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (8).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (9).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (10).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (11).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (12).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (13).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (14).png').convert_alpha(), True, False),
                  pygame.transform.flip(pygame.image.load('hit (15).png').convert_alpha(), True, False)]

enemy_left_land_hit = [pygame.image.load('land hit (1).png').convert_alpha(),
                       pygame.image.load('land hit (2).png').convert_alpha(),
                       pygame.image.load('land hit (3).png').convert_alpha(),
                       pygame.image.load('land hit (4).png').convert_alpha(),
                       pygame.image.load('land hit (5).png').convert_alpha(),
                       pygame.image.load('land hit (6).png').convert_alpha(),
                       pygame.image.load('land hit (7).png').convert_alpha(),
                       pygame.image.load('land hit (8).png').convert_alpha(),
                       pygame.image.load('land hit (9).png').convert_alpha(),
                       pygame.image.load('land hit (10).png').convert_alpha(),
                       pygame.image.load('land hit (11).png').convert_alpha(),
                       pygame.image.load('land hit (12).png').convert_alpha()]

enemy_right_land_hit = [pygame.transform.flip(pygame.image.load('land hit (1).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (2).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (3).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (4).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (5).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (6).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (7).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (8).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (9).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (10).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (11).png').convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load('land hit (12).png').convert_alpha(), True, False)]

enemy_left_rock = [pygame.image.load('rock shot (1).png').convert_alpha(),
                   pygame.image.load('rock shot (2).png').convert_alpha(),
                   pygame.image.load('rock shot (3).png').convert_alpha(),
                   pygame.image.load('rock shot (4).png').convert_alpha(),
                   pygame.image.load('rock shot (5).png').convert_alpha(),
                   pygame.image.load('rock shot (6).png').convert_alpha(),
                   pygame.image.load('rock shot (7).png').convert_alpha(),
                   pygame.image.load('rock shot (8).png').convert_alpha(),
                   pygame.image.load('rock shot (9).png').convert_alpha(),
                   pygame.image.load('rock shot (10).png').convert_alpha(),
                   pygame.image.load('rock shot (11).png').convert_alpha(),
                   pygame.image.load('rock shot (12).png').convert_alpha(),
                   pygame.image.load('rock shot (13).png').convert_alpha(),
                   pygame.image.load('rock shot (14).png').convert_alpha(),
                   pygame.image.load('rock shot (15).png').convert_alpha(),
                   pygame.image.load('rock shot (16).png').convert_alpha(),
                   pygame.image.load('rock shot (17).png').convert_alpha()]

enemy_right_rock = [pygame.transform.flip(pygame.image.load('rock shot (1).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (2).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (3).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (4).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (5).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (6).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (7).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (8).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (9).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (10).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (11).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (12).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (13).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (14).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (15).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (16).png').convert_alpha(), True, False),
                    pygame.transform.flip(pygame.image.load('rock shot (17).png').convert_alpha(), True, False)]

rock_teleport = [pygame.image.load('teleport rock (1).png').convert_alpha(),
                 pygame.image.load('teleport rock (2).png').convert_alpha(),
                 pygame.image.load('teleport rock (3).png').convert_alpha(),
                 pygame.image.load('teleport rock (4).png').convert_alpha(),
                 pygame.image.load('teleport rock (5).png').convert_alpha(),
                 pygame.image.load('teleport rock (6).png').convert_alpha(),
                 pygame.image.load('teleport rock (7).png').convert_alpha(),
                 pygame.image.load('teleport rock (8).png').convert_alpha(),
                 pygame.image.load('teleport rock (9).png').convert_alpha(),
                 pygame.image.load('teleport rock (10).png').convert_alpha(),
                 pygame.image.load('teleport rock (11).png').convert_alpha(),
                 pygame.image.load('teleport rock (12).png').convert_alpha(),
                 pygame.image.load('teleport rock (13).png').convert_alpha(),
                 pygame.image.load('teleport rock (14).png').convert_alpha(),
                 pygame.image.load('teleport rock (15).png').convert_alpha(),
                 pygame.image.load('teleport rock (16).png').convert_alpha(),
                 pygame.image.load('teleport rock (17).png').convert_alpha(),
                 pygame.image.load('teleport rock (18).png').convert_alpha(),
                 pygame.image.load('teleport rock (19).png').convert_alpha(),
                 pygame.image.load('teleport rock (20).png').convert_alpha(),
                 pygame.image.load('teleport rock (21).png').convert_alpha(),
                 pygame.image.load('teleport rock (22).png').convert_alpha(),
                 pygame.image.load('teleport rock (23).png').convert_alpha(),
                 pygame.image.load('teleport rock (24).png').convert_alpha(),
                 pygame.image.load('teleport rock (25).png').convert_alpha(),
                 pygame.image.load('teleport rock (26).png').convert_alpha(),
                 pygame.image.load('teleport rock (27).png').convert_alpha(),
                 pygame.image.load('teleport rock (28).png').convert_alpha(),
                 pygame.image.load('teleport rock (29).png').convert_alpha(),
                 pygame.image.load('teleport rock (30).png').convert_alpha(),
                 pygame.image.load('teleport rock (31).png').convert_alpha(),
                 pygame.image.load('teleport rock (32).png').convert_alpha(),
                 pygame.image.load('teleport rock (33).png').convert_alpha(),
                 pygame.image.load('teleport rock (34).png').convert_alpha(),
                 pygame.image.load('teleport rock (35).png').convert_alpha(),
                 pygame.image.load('teleport rock (36).png').convert_alpha(),
                 pygame.image.load('teleport rock (37).png').convert_alpha(),
                 pygame.image.load('teleport rock (38).png').convert_alpha(),
                 pygame.image.load('teleport rock (39).png').convert_alpha(),
                 pygame.image.load('teleport rock (40).png').convert_alpha(),
                 pygame.image.load('teleport rock (41).png').convert_alpha(),
                 pygame.image.load('teleport rock (42).png').convert_alpha(),
                 pygame.image.load('teleport rock (43).png').convert_alpha()]

teleported_rock = [pygame.image.load('teleported rock (1).png').convert_alpha(),
                   pygame.image.load('teleported rock (2).png').convert_alpha(),
                   pygame.image.load('teleported rock (3).png').convert_alpha(),
                   pygame.image.load('teleported rock (4).png').convert_alpha(),
                   pygame.image.load('teleported rock (5).png').convert_alpha(),
                   pygame.image.load('teleported rock (6).png').convert_alpha(),
                   pygame.image.load('teleported rock (7).png').convert_alpha(),
                   pygame.image.load('teleported rock (8).png').convert_alpha(),
                   pygame.image.load('teleported rock (9).png').convert_alpha(),
                   pygame.image.load('teleported rock (10).png').convert_alpha(),
                   pygame.image.load('teleported rock (11).png').convert_alpha(),
                   pygame.image.load('teleported rock (12).png').convert_alpha(),
                   pygame.image.load('teleported rock (13).png').convert_alpha(),
                   pygame.image.load('teleported rock (14).png').convert_alpha(),
                   pygame.image.load('teleported rock (15).png').convert_alpha(),
                   pygame.image.load('teleported rock (16).png').convert_alpha(),
                   pygame.image.load('teleported rock (17).png').convert_alpha(),
                   pygame.image.load('teleported rock (18).png').convert_alpha(),
                   pygame.image.load('teleported rock (19).png').convert_alpha(),
                   pygame.image.load('teleported rock (20).png').convert_alpha(),
                   pygame.image.load('teleported rock (21).png').convert_alpha(),
                   pygame.image.load('teleported rock (22).png').convert_alpha(),
                   pygame.image.load('teleported rock (23).png').convert_alpha(),
                   pygame.image.load('teleported rock (24).png').convert_alpha(),
                   pygame.image.load('teleported rock (25).png').convert_alpha(),
                   pygame.image.load('teleported rock (26).png').convert_alpha(),
                   pygame.image.load('teleported rock (27).png').convert_alpha(),
                   pygame.image.load('teleported rock (28).png').convert_alpha(),
                   pygame.image.load('teleported rock (29).png').convert_alpha(),
                   pygame.image.load('teleported rock (30).png').convert_alpha(),
                   pygame.image.load('teleported rock (31).png').convert_alpha(),
                   pygame.image.load('teleported rock (32).png').convert_alpha(),
                   pygame.image.load('teleported rock (33).png').convert_alpha()]

rock = [pygame.image.load('rock (1).png').convert_alpha(), pygame.image.load('rock (2).png').convert_alpha(),
        pygame.image.load('rock (3).png').convert_alpha(), pygame.image.load('rock (4).png').convert_alpha(),
        pygame.image.load('rock (5).png').convert_alpha(), pygame.image.load('rock (6).png').convert_alpha(),
        pygame.image.load('rock (7).png').convert_alpha(), pygame.image.load('rock (8).png').convert_alpha(),
        pygame.image.load('rock (9).png').convert_alpha(), pygame.image.load('rock (10).png').convert_alpha()]

land = [pygame.image.load('land (1).png').convert_alpha(), pygame.image.load('land (2).png').convert_alpha(),
        pygame.image.load('land (3).png').convert_alpha(), pygame.image.load('land (4).png').convert_alpha(),
        pygame.image.load('land (5).png').convert_alpha(), pygame.image.load('land (6).png').convert_alpha(),
        pygame.image.load('land (7).png').convert_alpha(), pygame.image.load('land (8).png').convert_alpha(),
        pygame.image.load('land (9).png').convert_alpha()]

lef_land = [pygame.transform.flip(pygame.image.load('land (1).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (2).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (3).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (4).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (5).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (6).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (7).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (8).png').convert_alpha(), True, False),
            pygame.transform.flip(pygame.image.load('land (9).png').convert_alpha(), True, False)]

enemy_win = [pygame.image.load('win (1).png').convert_alpha(), pygame.image.load('win (2).png').convert_alpha(),
             pygame.image.load('win (3).png').convert_alpha(),
             pygame.image.load('win (4).png').convert_alpha(), pygame.image.load('win (5).png').convert_alpha(),
             pygame.image.load('win (6).png').convert_alpha(),
             pygame.image.load('win (7).png').convert_alpha(), pygame.image.load('win (8).png').convert_alpha(),
             pygame.image.load('win (9).png').convert_alpha(),
             pygame.image.load('win (10).png').convert_alpha(), pygame.image.load('win (11).png').convert_alpha(),
             pygame.image.load('win (12).png').convert_alpha(),
             pygame.image.load('win (13).png').convert_alpha(),
             pygame.image.load('win (14).png').convert_alpha(), pygame.image.load('win (15).png').convert_alpha(),
             pygame.image.load('win (16).png').convert_alpha(), pygame.image.load('win (17).png').convert_alpha(),
             pygame.image.load('win (18).png').convert_alpha(),
             pygame.image.load('win (19).png').convert_alpha(), pygame.image.load('win (20).png').convert_alpha(),
             pygame.image.load('win (21).png').convert_alpha(),
             pygame.image.load('win (22).png').convert_alpha(), pygame.image.load('win (23).png').convert_alpha(),
             pygame.image.load('win (24).png').convert_alpha(),
             pygame.image.load('win (25).png').convert_alpha(), pygame.image.load('win (26).png').convert_alpha(),
             pygame.image.load('win (27).png').convert_alpha(),
             pygame.image.load('win (28).png').convert_alpha(), pygame.image.load('win (29).png').convert_alpha(),
             pygame.image.load('win (30).png').convert_alpha(),
             pygame.image.load('win (31).png').convert_alpha(), pygame.image.load('win (32).png').convert_alpha(),
             pygame.image.load('win (33).png').convert_alpha(),
             pygame.image.load('win (34).png').convert_alpha(), pygame.image.load('win (35).png').convert_alpha(),
             pygame.image.load('win (36).png').convert_alpha(),
             pygame.image.load('win (37).png').convert_alpha(), pygame.image.load('win (38).png').convert_alpha(),
             pygame.image.load('win (39).png').convert_alpha(),
             pygame.image.load('win (40).png').convert_alpha(), pygame.image.load('win (41).png').convert_alpha(),
             pygame.image.load('win (42).png').convert_alpha(),
             pygame.image.load('win (43).png').convert_alpha()]

enemyx = width - 550
enemyy = height - 155
en_health = 1000
enemy_hitbox = [0, 0, 0, 0]
e = 0
f = 0
enemy_sound = [mixer.Sound('stone_throw.wav'), mixer.Sound('stone_hit.wav'), mixer.Sound('rock_crashing.wav'),
               mixer.Sound('fire.wav'), mixer.Sound('land.wav')]
ischoice = True
long_range_list = ['teleport', 'long range hit', 'long range shot', 'long range teleport', 'walk']
combine_list = ['hit', 'teleport', 'long range hit', 'long range shot', 'long range teleport']
en_var = [0, 0, 9]

x = 0
y = 0
z = 0

playerX = 0 + 430
playerY = height - 120
pl_health = 1000
player_hitbox = [0, 0, 0, 0]
player_power_attack = 'none'
player_sound = [mixer.Sound('walk.wav'), mixer.Sound('unibeam.wav'), mixer.Sound("missile.wav"),
                mixer.Sound("launch.wav"), mixer.Sound("missile_hit.wav"), mixer.Sound('domo.wav'),
                mixer.Sound('iron_kick.wav'), mixer.Sound('ironman_hit.wav')]
wimg = 0
wimgchg = 0
down_ = 0
domo_ = 0
img = 0
dshi = 0
shi = 0
shi_chg = 0
fly = 0
fly_chg = 0
fight_img = 0
fight_chg_img = 0
beam_img = 0
beam_chg_img = 0
playerX_change = 0
playerY_change = 0
iswalkl = False
iswalkr = False
fly_ = False
plane = True
downkey = False
s_key = False
c_key = False
f_key = False
d_key = False
w_key = False
game_exit = True
intro_screen = True
pause = False
beam_var = 5
bg_var = 0
func = True
beam_help = False


def type(x, a, b, c, d, e, f, g):
    text = pygame.font.Font('freesansbold.ttf', f)
    line = text.render(x, True, (c, d, e))
    if g == True:
        get = line.get_rect()
        get.center = (int(a), int(b))
        screen.blit(line, get)
    else:
        screen.blit(line, (int(a), int(b)))


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def health(a, b, c, d):
    very_smallText = pygame.font.SysFont("comicsansms", 12)
    if pl_health >= 0:
        pygame.draw.rect(screen, (225 - int(pl_health / 5), 25 + int(pl_health / 5), 0), (a, b, int(pl_health / 5), 20))
        pygame.draw.rect(screen, (255, 255, 255), (a, b, 200, 20), 2)
        pl_bar, pl_get = text_objects("Iron Man : " + str(int(pl_health / 10)) + '%', very_smallText)
        pl_get.center = (int(int(a) + (int(200) / 2)), int(int(b) + (int(20) / 2)))
        screen.blit(pl_bar, pl_get)
    else:
        type('You lose', width / 2, height / 2, 255, 255, 255, 42, True)
    if en_health >= 0:
        pygame.draw.rect(screen, (225 - int(en_health / 5), 25 + int(en_health / 5), 0), (c, d, int(en_health / 5), 20))
        pygame.draw.rect(screen, (255, 255, 255), (c, d, 200, 20), 2)
        en_bar, en_get = text_objects("Thanos : " + str(int(en_health / 10)) + '%', very_smallText)
        en_get.center = (int(int(c) + (int(200) / 2)), int(int(d) + (int(20) / 2)))
        screen.blit(en_bar, en_get)
    else:
        type('You win', width / 2, height / 2, 255, 255, 255, 42, True)


enemy_weapon_x = []
enemy_weapon_y = []
enemy_var = []
enemy_weapon_pos = []
en_bull_arrary = []
number_of_weapon = 10
enemy_weapon_index = 0

for i in range(number_of_weapon):
    enemy_weapon_x.append(0)
    enemy_weapon_y.append(0)
    enemy_var.append(0)
    enemy_weapon_pos.append('none')
    en_bull_arrary.append([0, 0, 0, 0])

# Caption and Icon
pygame.display.set_caption("Iron Man")
icon = pygame.image.load('marvel.png')
pygame.display.set_icon(icon)

bulletImg = []
lef_bulletimg = []
bulletX = []
bulletY = []
bullet_state = []
num_of_bullets = 5
index = 0

for i in range(num_of_bullets):
    bulletImg.append(0)
    lef_bulletimg.append(0)
    bulletX.append(0)
    bulletY.append(playerY + 30)
    bullet_state.append('none')


def continues_bullet(index):
    global enemy_hitbox, en_health, beam_var, player_sound
    if bullet_state[index] == 'right':
        screen.blit(bulletImg[index], (bulletX[index], bulletY[index]))
        bulletX[index] += 30
        if bulletX[index] < enemy_hitbox[0] + enemy_hitbox[2] and bulletX[index] + 90 > enemy_hitbox[0]:
            if bulletY[index] < enemy_hitbox[1] + enemy_hitbox[3] and bulletY[index] + 24 > enemy_hitbox[1]:
                player_sound[4].play()
                player_sound[4].set_volume(.3)
                en_health -= 3
                beam_var += 1
                bulletImg[index] = 0
                bullet_state[index] = 'none'
        elif bulletX[index] >= width:
            bulletImg[index] = 0
            bullet_state[index] = 'none'
    if bullet_state[index] == 'left':
        screen.blit(lef_bulletimg[index], (bulletX[index], bulletY[index]))
        bulletX[index] -= 30
        if bulletX[index] + 90 > enemy_hitbox[0] + enemy_hitbox[2] and bulletX[index] < enemy_hitbox[0] + enemy_hitbox[
            2]:
            if bulletY[index] < enemy_hitbox[1] + enemy_hitbox[3] and bulletY[index] + 24 > enemy_hitbox[1]:
                player_sound[4].play()
                player_sound[4].set_volume(.3)
                en_health -= 3
                beam_var += 1
                lef_bulletimg[index] = 0
                bullet_state[index] = 'none'
        elif bulletX[index] <= 0:
            lef_bulletimg[index] = 0
            bullet_state[index] = 'none'


beam = pygame.image.load('beam.png').convert_alpha()
lef_beam = pygame.transform.flip(pygame.image.load('beam.png').convert_alpha(), True, False)
beamy = playerY
beamtemp = 0
beamstate = 'none'
beamsize = 10


def beam_state(beamstate, beamx):
    global beamtemp, beamsize, beam, lef_beam, beamy, player_power_attack, en_health
    if beamstate == 'right':
        beam = pygame.transform.scale(beam, (beamsize, 44))
        screen.blit(beam, (beamx, beamy))
        if beamy < enemy_hitbox[1] + enemy_hitbox[3] and beamy + 44 > enemy_hitbox[1] and beamx + beamsize - 50 > \
                enemy_hitbox[0] and beamx + beamsize - 50 < enemy_hitbox[0] + enemy_hitbox[2]:
            en_health -= 5
            player_power_attack = 'beam'
            beamtemp = 0
            beamsize += beamtemp
        else:
            beamtemp = 50
            beamsize += beamtemp
    elif beamstate == 'left':
        lef_beam = pygame.transform.scale(lef_beam, (beamsize, 44))
        beamx -= beamsize
        screen.blit(lef_beam, (beamx, beamy))
        if beamy < enemy_hitbox[1] + enemy_hitbox[3] and beamy + 44 > enemy_hitbox[1] and beamx + 150 > enemy_hitbox[
            0] and beamx + 150 < enemy_hitbox[0] + enemy_hitbox[2]:
            en_health -= 5
            player_power_attack = 'beam'
            beamtemp = 0
            beamsize += beamtemp
        else:
            beamtemp = 50
            beamsize += beamtemp
    elif beamstate == 'none':
        beamtemp = 0
        beamsize = 10
        player_power_attack = 'none'


# msg: What do you want the button to say on it.
# x: The x location of the top left coordinate of the button box.
# y: The y location of the top left coordinate of the button box.
# w: Button width.
# h: Button height.
# ic: Inactive color (when a mouse is not hovering).
# ac: Active color (when a mouse is hovering).
def button(msg, x, y, w, h, ic, ac, action=None):
    global game_exit
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if int(x) + int(w) > mouse[0] > int(x) and int(y) + int(h) > mouse[1] > int(y):
        pygame.draw.rect(screen, ac, (int(x), int(y), int(w), (h)))

        if click[0] == 1 and action != None:
            action()
            if action == gameloop:
                game_exit = False
                action()
    else:
        pygame.draw.rect(screen, ic, (int(x), int(y), int(w), int(h)))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (int(int(x) + (int(w) / 2)), int(int(y) + (int(h) / 2)))
    screen.blit(textSurf, textRect)


def intro():
    mixer.music.load("intro bgm.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.4)
    global game_exit, intro_screen

    while intro_screen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_screen = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    game_exit = False
                    intro_screen = False
                    gameloop()
        clock.tick(18)
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(background[3], (width, height)), (0, 0))
        type('Iron Man', width * 0.7, height * .1, 225, 0, 0, 100, False)
        type('by Kameswaran', width * 0.72, height * .21, 224, 224, 224, 22, False)
        type('press Enter to start, ESC to', width * 0.72, height * .42, 58, 144, 255, 32, False)
        type('quit, Space bar to pause', width * 0.72, height * .46, 58, 144, 255, 32, False)
        type('for development contact', width * 0.72, height * .52, 224, 224, 224, 22, False)
        type('kameshwaraniyanar@gmail.com', width * 0.72, height * .55, 224, 224, 224, 22, False)
        button("START", width * .15, height * .52, 100, 50, (0, 200, 0), (0, 255, 0), gameloop)
        button("Quit", width * .15, height * .72, 100, 50, (200, 0, 0), (255, 0, 0), quitgame)
        button("Help", width * .15, height * .62, 100, 50, (0, 0, 200), (0, 0, 255), gamehelp)
        pygame.display.flip()


def gamehelp():
    global func, game_exit
    while func:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                func = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    game_exit = False
                    func = False
                    gameloop()

        clock.tick(15)
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(background[5], (width, height)), (0, 0))
        type('Welcome to Iron Man', width / 2, height * .1, 255, 255, 0, 42, True)
        type('e key = shot missile', width * .2, height * .25, 0, 225, 225, 25, False)
        type('w key = blast beam', width * .2, height * .3, 0, 225, 225, 25, False)
        type('s key = shield', width * .2, height * .35, 0, 225, 225, 25, False)
        type('c key = kick', width * .2, height * .4, 0, 225, 225, 25, False)
        type('d key = fight', width * .2, height * .45, 0, 225, 225, 25, False)
        type('Up Arrow = fly', width * .2, height * .5, 0, 225, 225, 25, False)
        type('Down Arrow = sit on floor', width * .2, height * .55, 0, 225, 225, 25, False)
        type('Right Arrow = move right', width * .2, height * .6, 0, 225, 225, 25, False)
        type('Left Arrow = move left', width * .2, height * .65, 0, 225, 225, 25, False)
        type('Note:', width * .5, height * .2, 0, 255, 0, 32, False)
        type('  1. Use the arrow key with e, w, s, c and d to get combine result.', width * .5, height * .25, 255, 255,
             255, 22, False)
        type('  2. Kick option (c key) is only available attack while in flight.', width * .5, height * .35, 255, 255,
             255, 22, False)
        type('  3. You can\'t use the beam continuously. In starting you can use but', width * .5, height * .45, 255,
             255, 255, 22, False)
        type('  after removing your hand from w key, you have to shot or attack', width * .5, height * .5, 255, 255,
             255, 22, False)
        type('  thanos for 5 times, then only you can use beam.', width * .5, height * .55, 255, 255, 255, 22, False)
        type('  Thanks to \'fightersgeneration.com\' for animated gif files', width * .5, height * .65, 0, 255, 255, 26,
             False)
        button("START", width / 2, height * .8, 100, 50, (0, 200, 0), (0, 255, 0), gameloop)
        button("Return", width * .15, height * .8, 100, 50, (200, 200, 0), (255, 255, 0), intro)
        pygame.display.update()


def quitgame():
    pygame.quit()
    quit()


def paused():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    pause = False
                    gameloop()
                if event.key == pygame.K_SPACE:
                    pause = False
                    gameloop()
        clock.tick(18)
        # screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(background[4], (width, height)), (0, 0))
        type('Paused', int(width / 2), int(height / 2), 224, 244, 244, 150, True)
        button("GO!", width * .15, height * .52, 100, 50, (0, 200, 0), (0, 255, 0), gameloop)
        button("Quit", width * .8, height * .52, 100, 50, (200, 0, 0), (255, 0, 0), quitgame)
        pygame.display.flip()


def math(a, pos):
    global index
    index += 1
    if index >= num_of_bullets:
        index = 0
    if pos == 'right':
        bulletImg[index] = pygame.image.load('bullet.png').convert_alpha()
    elif pos == 'left':
        lef_bulletimg[index] = pygame.transform.flip(pygame.image.load('bullet.png').convert_alpha(), True, False)
    bulletX[index] = a + 40
    bullet_state[index] = pos
    return index


def attack(j):
    global player_hitbox, enemy_hitbox, iswalkl, fly_, en_health, beam_var
    if iswalkl and enemy_hitbox[0] <= player_hitbox[0] and enemy_hitbox[0] + enemy_hitbox[2] <= player_hitbox[0] + \
            player_hitbox[2] and player_hitbox[1] < enemy_hitbox[1] + enemy_hitbox[3] and player_hitbox[1] + \
            player_hitbox[3] > enemy_hitbox[1]:
        if j <= 10:
            # print('hit')
            en_health -= 3
            beam_var += 1
        else:
            # print('complete')
            en_health -= 0
    elif enemy_hitbox[0] <= player_hitbox[0] + player_hitbox[2] and player_hitbox[0] <= enemy_hitbox[0] and \
            player_hitbox[1] < enemy_hitbox[1] + enemy_hitbox[3] and player_hitbox[1] + player_hitbox[3] > enemy_hitbox[
        1]:
        if j <= 10:
            # print('hit')
            en_health -= 3
            beam_var += 1
        else:
            # print('complete')
            en_health -= 0
    elif enemy_hitbox[0] <= player_hitbox[0] and enemy_hitbox[0] + enemy_hitbox[2] <= player_hitbox[0] + player_hitbox[
        2] or enemy_hitbox[0] <= player_hitbox[0] + player_hitbox[2] and player_hitbox[0] <= enemy_hitbox[0] or \
            player_hitbox[0] > enemy_hitbox[0] and player_hitbox[0] + player_hitbox[2] <= enemy_hitbox[0] + \
            enemy_hitbox[2]:
        if not plane and enemy_hitbox[1] <= player_hitbox[1] and enemy_hitbox[1] + enemy_hitbox[3] >= player_hitbox[1]:
            if j <= 10:
                # print('hit')
                en_health -= 3
                beam_var += 1
            else:
                # print('complete')
                en_health -= 0


def en_bulletbox(a, b, c, d, e):
    global en_bull_arrary
    en_bull_arrary[e] = [a, b, c, d]
    # pygame.draw.rect(screen, (255, 255, 255), (a, b, c, d), 2)


def tele(a):
    en_var[0] = a + 78
    en_var[1] = a - 118
    if enemyx < playerX <= enemyx + 120 or playerX + 80 >= enemyx > playerX:
        en_var[0] = a + 500
        en_var[1] = a - 500
        if en_var[0] <= 0 or en_var[1] <= 0:
            en_var[0] = 0
            en_var[1] = 0
        elif en_var[0] + 120 >= width or en_var[1] + 120 >= width:
            en_var[0] = width - 140
            en_var[1] = width - 140
    return en_var


def en_math(a, b, c):
    global enemy_weapon_index
    enemy_weapon_index += 1
    if enemy_weapon_index >= number_of_weapon:
        enemy_weapon_index = 0
    enemy_weapon_x[enemy_weapon_index] = a
    enemy_weapon_y[enemy_weapon_index] = b
    enemy_weapon_pos[enemy_weapon_index] = c
    enemy_var[enemy_weapon_index] = 0
    return enemy_weapon_index


def end(a, b, c):
    screen.blit(rock[c + 3], (a, b))


def rock_teleportation(enemy_weapon_index):
    global player_hitbox, en_bull_arrary, pl_health, enemy_sound
    if enemy_weapon_pos[enemy_weapon_index] == 'intermediate':
        enemy_sound[2].play()
        enemy_sound[2].set_volume(.2)
        enemy_var[enemy_weapon_index] += 1
        if en_bull_arrary[enemy_weapon_index][0] < player_hitbox[0] < en_bull_arrary[enemy_weapon_index][0] + \
                en_bull_arrary[enemy_weapon_index][2] or en_bull_arrary[enemy_weapon_index][0] < player_hitbox[0] + \
                player_hitbox[2] < en_bull_arrary[enemy_weapon_index][0] + en_bull_arrary[enemy_weapon_index][2]:
            if en_bull_arrary[enemy_weapon_index][1] < player_hitbox[1] < en_bull_arrary[enemy_weapon_index][1] + \
                    en_bull_arrary[enemy_weapon_index][3] or en_bull_arrary[enemy_weapon_index][1] < player_hitbox[1] + \
                    player_hitbox[3] < en_bull_arrary[enemy_weapon_index][1] + en_bull_arrary[enemy_weapon_index][3]:
                # print('hit')
                pl_health -= 3
                enemy_sound[1].play()
                enemy_sound[1].set_volume(.4)
        if enemy_var[enemy_weapon_index] >= 32:
            enemy_sound[2].stop()
            enemy_weapon_pos[enemy_weapon_index] = 'none'
            enemy_var[enemy_weapon_index] = 0
        en_bulletbox(enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index], 160, 231,
                     enemy_weapon_index)
        screen.blit(teleported_rock[enemy_var[enemy_weapon_index]],
                    (enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index]))
    if enemy_weapon_pos[enemy_weapon_index] == 'rock shot left':
        enemy_var[enemy_weapon_index] += 1
        enemy_weapon_x[enemy_weapon_index] -= 30
        if player_hitbox[0] + player_hitbox[2] >= en_bull_arrary[enemy_weapon_index][0] > player_hitbox[0] and \
                player_hitbox[1] < en_bull_arrary[enemy_weapon_index][1] + en_bull_arrary[enemy_weapon_index][3] and \
                en_bull_arrary[enemy_weapon_index][1] < player_hitbox[1] + player_hitbox[3]:
            if player_power_attack == 'right shield':
                pl_health -= 0
            else:
                pl_health -= 3
            enemy_weapon_pos[enemy_weapon_index] = 'ren_end'
        elif enemy_weapon_x[enemy_weapon_index] <= 0:
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        elif enemy_var[enemy_weapon_index] >= 2:
            enemy_var[enemy_weapon_index] = 0
        en_bulletbox(enemy_weapon_x[enemy_weapon_index] + 50, enemy_weapon_y[enemy_weapon_index] + 20, 70, 70,
                     enemy_weapon_index)
        screen.blit(rock[enemy_var[enemy_weapon_index]],
                    (enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index]))
    if enemy_weapon_pos[enemy_weapon_index] == 'rock shot right':
        enemy_var[enemy_weapon_index] += 1
        enemy_weapon_x[enemy_weapon_index] += 30
        if player_hitbox[0] + player_hitbox[2] >= en_bull_arrary[enemy_weapon_index][0] + \
                en_bull_arrary[enemy_weapon_index][2] > player_hitbox[0] and player_hitbox[1] < \
                en_bull_arrary[enemy_weapon_index][1] + en_bull_arrary[enemy_weapon_index][3] and \
                en_bull_arrary[enemy_weapon_index][1] < player_hitbox[1] + player_hitbox[3]:
            if player_power_attack == 'left shield':
                pl_health -= 0
            else:
                pl_health -= 3
            enemy_weapon_pos[enemy_weapon_index] = 'ren_end'
        elif enemy_weapon_x[enemy_weapon_index] >= width:
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        elif enemy_var[enemy_weapon_index] >= 2:
            enemy_var[enemy_weapon_index] = 0
        en_bulletbox(enemy_weapon_x[enemy_weapon_index] + 50, enemy_weapon_y[enemy_weapon_index] + 20, 70, 70,
                     enemy_weapon_index)
        screen.blit(rock[enemy_var[enemy_weapon_index]],
                    (enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index]))
    if enemy_weapon_pos[enemy_weapon_index] == 'land left':
        enemy_sound[4].play()
        enemy_sound[4].set_volume(.07)
        enemy_var[enemy_weapon_index] += 1
        enemy_weapon_x[enemy_weapon_index] -= 30
        if player_hitbox[0] + player_hitbox[2] >= en_bull_arrary[enemy_weapon_index][0] > player_hitbox[0] and \
                player_hitbox[1] < en_bull_arrary[enemy_weapon_index][1] + en_bull_arrary[enemy_weapon_index][3] and \
                en_bull_arrary[enemy_weapon_index][1] < player_hitbox[1] + player_hitbox[3]:
            if player_power_attack == 'right shield':
                pl_health -= 0
            else:
                pl_health -= 3
            enemy_sound[4].stop()
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        elif enemy_weapon_x[enemy_weapon_index] <= 0:
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        elif enemy_var[enemy_weapon_index] >= 8:
            enemy_var[enemy_weapon_index] = 0
        en_bulletbox(enemy_weapon_x[enemy_weapon_index] + 80, enemy_weapon_y[enemy_weapon_index] + 50, 200, 145,
                     enemy_weapon_index)
        screen.blit(land[enemy_var[enemy_weapon_index]],
                    (enemy_weapon_x[enemy_weapon_index] + 80, enemy_weapon_y[enemy_weapon_index]))
    if enemy_weapon_pos[enemy_weapon_index] == 'land right':
        enemy_sound[4].play()
        enemy_sound[4].set_volume(.07)
        enemy_var[enemy_weapon_index] += 1
        enemy_weapon_x[enemy_weapon_index] += 30
        if player_hitbox[0] + player_hitbox[2] >= en_bull_arrary[enemy_weapon_index][0] + \
                en_bull_arrary[enemy_weapon_index][2] > player_hitbox[0] and player_hitbox[1] < \
                en_bull_arrary[enemy_weapon_index][1] + en_bull_arrary[enemy_weapon_index][3] and \
                en_bull_arrary[enemy_weapon_index][1] < player_hitbox[1] + player_hitbox[3]:
            if player_power_attack == 'left shield':
                pl_health -= 0
            else:
                pl_health -= 3
            enemy_sound[4].stop()
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        elif enemy_weapon_x[enemy_weapon_index] >= width:
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        elif enemy_var[enemy_weapon_index] >= 8:
            enemy_var[enemy_weapon_index] = 0
        en_bulletbox(enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index] + 50, 200, 145,
                     enemy_weapon_index)
        screen.blit(lef_land[enemy_var[enemy_weapon_index]],
                    (enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index]))
    if enemy_weapon_pos[enemy_weapon_index] == 'ren_end':
        enemy_sound[1].play()
        enemy_sound[1].set_volume(.4)
        global f
        f += 1
        enemy_weapon_y[enemy_weapon_index] += 5
        if f >= 6:
            f = 0
            enemy_sound[1].stop()
            enemy_weapon_pos[enemy_weapon_index] = 'none'
        end(enemy_weapon_x[enemy_weapon_index], enemy_weapon_y[enemy_weapon_index], f)
    if enemy_weapon_pos[enemy_weapon_index] == 'none':
        en_bull_arrary[enemy_weapon_index] = [0, 0, 0, 0]


def en_hitbox(a, b, c, d):
    global enemy_hitbox
    enemy_hitbox = [a, b, c, d]
    # pygame.draw.rect(screen, (255, 255, 255), (a, b, c, d), 2)


def pl_hitbox(a, b, c, d):
    global player_hitbox
    player_hitbox = [a, b, c, d]
    # pygame.draw.rect(screen, (255, 255, 255), (a, b, c, d), 2)


def enemy(choice, a, b):
    global enemyx, enemyy, ischoice, e, enemy_weapon_index, en_var, pl_health, x, enemy_sound

    if en_health <= 0:
        pass
    elif pl_health <= 0:
        x += 1
        if x >= 42:
            x = 30
        if x <= 24:
            screen.blit(enemy_win[x], (enemyx, enemyy - 70))
        else:
            screen.blit(enemy_win[x], (enemyx, enemyy - 55))
    elif player_power_attack == 'beam':
        ischoice = False
        enemyx += 0
        enemyy += 0
        e += 1
        if e >= 25:
            e = 0
            ischoice = True
        if playerX <= enemyx:
            en_hitbox(enemyx, enemyy, 140, 140)
            screen.blit(enemy_left_stand[e], (enemyx, enemyy))
        elif playerX > enemyx:
            en_hitbox(enemyx, enemyy, 140, 140)
            screen.blit(enemy_right_stand[e], (enemyx, enemyy))
    elif choice == 'walk':
        ischoice = False
        e += 1
        if e >= 8:
            e = 0
            ischoice = True
        if playerX + 80 < enemyx:
            enemyx -= 6
            en_hitbox(enemyx, enemyy, 130, 140)
            screen.blit(enemy_left_walk[e], (enemyx, enemyy))
        elif playerX > enemyx + 120:
            enemyx += 6
            en_hitbox(enemyx, enemyy, 130, 140)
            screen.blit(enemy_right_walk[e], (enemyx, enemyy))
        elif enemyx < playerX <= enemyx + 120:
            enemyx += 0
            en_hitbox(enemyx, enemyy, 140, 140)
            screen.blit(enemy_right_stand[e], (enemyx, enemyy))
        elif playerX + 80 >= enemyx > playerX:
            enemyx += 0
            en_hitbox(enemyx, enemyy, 140, 140)
            screen.blit(enemy_left_stand[e], (enemyx, enemyy))
    elif choice == 'teleport':
        ischoice = False
        en_var[2] -= 1
        if en_var[2] == 7:
            tele(a)
        if en_var[2] <= 0:
            en_var[2] = 0
            e += 1
            if e >= 9:
                e = 0
                en_var[2] = 9
                ischoice = True
            if playerX <= enemyx:
                enemyx = en_var[0]
                en_hitbox(enemyx + 15, enemyy - 10, 140, 140)
                screen.blit(teleport_left[e], (enemyx, enemyy - 35))
            elif playerX > enemyx:
                enemyx = en_var[1]
                en_hitbox(enemyx + 15, enemyy - 10, 140, 140)
                screen.blit(teleport_right[e], (enemyx, enemyy - 35))
        if playerX <= enemyx:
            en_hitbox(enemyx + 15, enemyy - 10, 140, 140)
            screen.blit(teleport_left[en_var[2]], (enemyx, enemyy - 35))
        elif playerX > enemyx:
            en_hitbox(enemyx + 15, enemyy - 10, 140, 140)
            screen.blit(teleport_right[en_var[2]], (enemyx, enemyy - 35))
    elif choice == 'hit':
        ischoice = False
        e += 1
        enemy_sound[3].play()
        enemy_sound[3].set_volume(.05)
        if e >= 14:
            e = 0
            ischoice = True
            enemy_sound[3].stop()
        if playerX <= enemyx:
            en_hitbox(enemyx + 20, enemyy, 260, 140)
            screen.blit(enemy_left_hit[e], (enemyx, enemyy - 30))
            if e >= 2:
                if enemy_hitbox[1] < player_hitbox[1] < enemy_hitbox[1] + enemy_hitbox[3] or enemy_hitbox[1] < \
                        player_hitbox[1] + player_hitbox[3] < enemy_hitbox[1] + enemy_hitbox[3]:
                    if enemy_hitbox[0] < player_hitbox[0] + player_hitbox[2] < enemy_hitbox[0] + enemy_hitbox[2]:
                        # print('hit')
                        if player_power_attack == 'right shield':
                            pl_health -= 0
                        else:
                            pl_health -= 3
        elif playerX > enemyx:
            en_hitbox(enemyx + 50, enemyy, 260, 140)
            screen.blit(enemy_right_hit[e], (enemyx, enemyy - 30))
            if e >= 2:
                if enemy_hitbox[1] < player_hitbox[1] < enemy_hitbox[1] + enemy_hitbox[3] or enemy_hitbox[1] < \
                        player_hitbox[1] + player_hitbox[3] < enemy_hitbox[1] + enemy_hitbox[3]:
                    if enemy_hitbox[0] < player_hitbox[0] < enemy_hitbox[0] + enemy_hitbox[2]:
                        # print('hit')
                        if player_power_attack == 'left shield':
                            pl_health -= 0
                        else:
                            pl_health -= 3
    elif choice == 'long range hit':
        ischoice = False
        enemy_sound[4].play()
        enemy_sound[4].set_volume(.07)
        e += 1
        if e >= 11:
            e = 0
            ischoice = True
        if playerX <= enemyx:
            if e == 3:
                c = 'land left'
                en_math(enemyx, enemyy, c)
            en_hitbox(enemyx + 200, enemyy - 20, 140, 160)
            screen.blit(enemy_left_land_hit[e], (enemyx, enemyy - 30))
        elif playerX > enemyx:
            if e == 3:
                c = 'land right'
                en_math(enemyx, enemyy, c)
            en_hitbox(enemyx, enemyy - 20, 140, 160)
            screen.blit(enemy_right_land_hit[e], (enemyx, enemyy - 30))
    elif choice == 'long range shot':
        enemy_sound[0].play()
        enemy_sound[0].set_volume(.1)
        ischoice = False
        e += 1
        if e >= 16:
            e = 0
            ischoice = True
        if playerX <= enemyx:
            if e == 6:
                c = 'rock shot left'
                en_math(enemyx, enemyy, c)
                enemy_sound[0].stop()
            en_hitbox(enemyx + 5, enemyy + 5, 180, 140)
            screen.blit(enemy_left_rock[e], (enemyx, enemyy - 45))
        elif playerX > enemyx:
            if e == 6:
                c = 'rock shot right'
                en_math(enemyx + 10, enemyy, c)
                enemy_sound[0].stop()
            en_hitbox(enemyx + 5, enemyy + 5, 180, 140)
            screen.blit(enemy_right_rock[e], (enemyx, enemyy - 45))
    elif choice == 'long range teleport':
        ischoice = False
        enemy_sound[2].play()
        enemy_sound[2].set_volume(.2)
        e += 1
        if e >= 42:
            e = 0
            ischoice = True
        if e == 38:
            c = 'intermediate'
            en_math(a, b - 80, c)
        en_hitbox(enemyx + 100, enemyy - 45, 140, 180)
        screen.blit(rock_teleport[e], (enemyx, enemyy - 80))

    for i in range(number_of_weapon):
        rock_teleportation(i)


def player(a, b, c, d, e, f, g, h, i, j, k):
    global player_power_attack, y, z, beam_var, player_sound
    if en_health <= 0:
        y += 1
        if y >= 21:
            y = 6
        screen.blit(ironman_win[y], (a - 35, height - 220))
    elif pl_health <= 0:
        z += 1
        if z >= 18:
            z = 8
        screen.blit(dead[z], (a - 35, height - 140))
    elif w_key and plane and iswalkr:
        pl_hitbox(a + 5, b, 110, 100)
        screen.blit(chest_beam[k], (a - 35, b - 100))
        player_sound[1].play()
        player_sound[1].set_volume(0.05)
        if 9 <= k <= 47:
            beamx = int(a + 80)
            beamstate = 'right'
            beam_state(beamstate, beamx)
            beam_var = 0
        else:
            beamx = int(a + 80)
            beamstate = 'none'
            beam_state(beamstate, beamx)
    elif w_key and plane and iswalkl:
        pl_hitbox(a + 90, b, 110, 100)
        screen.blit(rev_chest_beam[k], (a - 35, b - 100))
        player_sound[1].play()
        player_sound[1].set_volume(0.05)
        if 9 <= k <= 47:
            beamx = int(a + 130)
            beamstate = 'left'
            beam_state(beamstate, beamx)
            beam_var = 0
        else:
            beamx = int(a + 130)
            beamstate = 'none'
            beam_state(beamstate, beamx)
    elif w_key and plane:
        pl_hitbox(a + 5, b, 110, 100)
        screen.blit(chest_beam[k], (a - 35, b - 100))
        player_sound[1].play()
        player_sound[1].set_volume(0.05)
        if 9 <= k <= 47:
            beamx = int(a + 80)
            beamstate = 'right'
            beam_state(beamstate, beamx)
            beam_var = 0
        else:
            beamx = int(a + 80)
            beamstate = 'none'
            beam_state(beamstate, beamx)
    elif c_key and plane and iswalkr and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 15, b + 35, 160, 70)
        attack(j)
        screen.blit(fight[4 * 12 + j], (a, b - 20))
    elif c_key and plane and iswalkl and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 90, b + 35, 160, 70)
        attack(j)
        screen.blit(rev_fight[4 * 12 + j], (a, b - 20))
    elif c_key and plane and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 15, b + 35, 160, 70)
        attack(j)
        screen.blit(fight[4 * 12 + j], (a, b - 20))
    elif f_key and plane and iswalkr and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 5, b + 30, 110, 80)
        screen.blit(fight[6 * 12 + j], (a - 30, b - 35))
        if j == 4:
            player_sound[2].play()
            player_sound[2].set_volume(0.3)
            pos = 'right'
            math(a, pos)
    elif f_key and plane and iswalkl and downkey:
        player_power_attack = 'none'
        pl_hitbox(a - 25, b + 25, 110, 80)
        screen.blit(rev_fight[6 * 12 + j], (a - 30, b - 35))
        if j == 4:
            player_sound[2].play()
            player_sound[2].set_volume(0.3)
            pos = 'left'
            math(a, pos)
    elif f_key and plane and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 5, b + 30, 110, 80)
        screen.blit(fight[6 * 12 + j], (a - 30, b - 35))
        if j == 4:
            player_sound[2].play()
            player_sound[2].set_volume(0.3)
            pos = 'right'
            math(a, pos)
    elif d_key and plane and iswalkr and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 10, b - 10, 120, 120)
        attack(j)
        screen.blit(fight[5 * 12 + j], (a - 30, b - 35))
    elif d_key and plane and iswalkl and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 140, b - 10, 120, 120)
        attack(j)
        screen.blit(rev_fight[5 * 12 + j], (a - 30, b - 35))
    elif d_key and plane and downkey:
        player_power_attack = 'none'
        pl_hitbox(a + 10, b - 10, 120, 120)
        attack(j)
        screen.blit(fight[5 * 12 + j], (a - 30, b - 35))
    elif f_key and plane and iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a, b, 110, 100)
        screen.blit(fight[1 * 12 + j], (a, b))
        if j == 4:
            player_sound[2].play()
            player_sound[2].set_volume(0.3)
            pos = 'right'
            math(a, pos)
    elif f_key and plane and iswalkl:
        player_power_attack = 'none'
        pl_hitbox(a, b, 200, 100)
        screen.blit(rev_fight[1 * 12 + j], (a, b))
        if j == 4:
            player_sound[2].play()
            player_sound[2].set_volume(0.3)
            pos = 'left'
            math(a, pos)
    elif f_key and plane:
        player_power_attack = 'none'
        pl_hitbox(a, b, 110, 100)
        screen.blit(fight[1 * 12 + j], (a, b))
        if j == 4:
            player_sound[2].play()
            player_sound[2].set_volume(0.3)
            pos = 'right'
            math(a, pos)
    elif d_key and plane and iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a, b, 145, 100)
        attack(j)
        screen.blit(fight[0 * 12 + j], (a, b))
    elif d_key and plane and iswalkl:
        player_power_attack = 'none'
        pl_hitbox(a - 5, b, 145, 100)
        attack(j)
        screen.blit(rev_fight[0 * 12 + j], (a, b))
    elif d_key and plane:
        player_power_attack = 'none'
        pl_hitbox(a, b, 145, 100)
        attack(j)
        screen.blit(fight[0 * 12 + j], (a, b))
    elif c_key and iswalkr and fly_:
        player_power_attack = 'none'
        pl_hitbox(a, b, 95, 185)
        attack(j)
        screen.blit(fight[3 * 12 + j], (a, b))
    elif c_key and iswalkl and fly_:
        player_power_attack = 'none'
        pl_hitbox(a, b, 95, 185)
        attack(j)
        screen.blit(rev_fight[3 * 12 + j], (a, b))
    elif c_key and fly_:
        player_power_attack = 'none'
        pl_hitbox(a, b, 95, 185)
        attack(j)
        screen.blit(fight[3 * 12 + j], (a, b))
    elif c_key and plane and iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a, b, 185, 95)
        attack(j)
        screen.blit(fight[2 * 12 + j], (a, b))
    elif c_key and plane and iswalkl:
        player_power_attack = 'none'
        pl_hitbox(a, b, 270, 95)
        attack(j)
        screen.blit(rev_fight[2 * 12 + j], (a, b))
    elif c_key and plane:
        player_power_attack = 'none'
        pl_hitbox(a, b, 185, 95)
        attack(j)
        screen.blit(fight[2 * 12 + j], (a, b))
    elif plane and s_key and iswalkr and downkey:
        pl_hitbox(a, b + 20, 120, 80)
        screen.blit(down_shield[i], (a, b + 20))
        player_power_attack = 'right shield'
    elif plane and s_key and iswalkl and downkey:
        pl_hitbox(a, b + 20, 120, 80)
        screen.blit(rev_down_shield[i], (a, b + 20))
        player_power_attack = 'left shield'
    elif plane and s_key and downkey:
        pl_hitbox(a, b + 20, 120, 80)
        screen.blit(down_shield[i], (a, b + 20))
        player_power_attack = 'right shield'
    elif plane and s_key and iswalkr:
        pl_hitbox(a, b - 20, 90, 130)
        screen.blit(shield[h], (a, b - 20))
        player_power_attack = 'right shield'
    elif plane and s_key and iswalkl:
        pl_hitbox(a, b - 20, 90, 130)
        screen.blit(rev_shield[h], (a, b - 20))
        player_power_attack = 'left shield'
    elif plane and s_key:
        pl_hitbox(a, b - 20, 90, 130)
        screen.blit(shield[h], (a, b - 20))
        player_power_attack = 'right shield'
    elif fly_ and iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a, b, 90, 110)
        screen.blit(rfly[e], (a, b))
    elif fly_ and iswalkl:
        player_power_attack = 'none'
        pl_hitbox(a, b, 90, 110)
        screen.blit(lfly[e], (a, b))
    elif iswalkl and iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a, b, 100, 100)
        screen.blit(stand[c], (a, b))
    elif downkey and plane and iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a + 15, b + 40, 160, 70)
        screen.blit(domo[g], (a, b - 5))
        player_sound[5].play()
        player_sound[5].set_volume(.1)
    elif downkey and plane and iswalkl:
        player_power_attack = 'none'
        pl_hitbox(a + 100, b + 40, 160, 70)
        screen.blit(revdomo[g], (a, b - 5))
        player_sound[5].play()
        player_sound[5].set_volume(.1)
    elif downkey and plane:
        player_power_attack = 'none'
        pl_hitbox(a, b + 35, 110, 70)
        screen.blit(down[f], (a, b + 35))
    elif not fly_ and iswalkl and not plane:
        player_power_attack = 'none'
        pl_hitbox(a, b, 100, 100)
        screen.blit(revstand[c], (a, b))
    elif not fly_ and iswalkr and not plane:
        player_power_attack = 'none'
        pl_hitbox(a, b, 100, 100)
        screen.blit(stand[c], (a, b))
    elif iswalkr:
        player_power_attack = 'none'
        pl_hitbox(a, b - 10, 70, 110)
        screen.blit(walk[d], (a, b - 10))
        player_sound[0].play()
        player_sound[0].set_volume(.3)
    elif iswalkl:
        player_power_attack = 'none'
        pl_hitbox(a, b - 10, 70, 110)
        screen.blit(rev[d], (a, b - 10))
        player_sound[0].play()
        player_sound[0].set_volume(.3)
    elif fly_:
        player_power_attack = 'none'
        pl_hitbox(a, b, 90, 110)
        screen.blit(rfly[e], (a, b))
    elif not fly_:
        player_power_attack = 'none'
        pl_hitbox(a, b, 100, 100)
        screen.blit(stand[c], (a, b))

    if fly_ and iswalkr or fly_ and iswalkl or fly_:
        player_sound[3].play()
        player_sound[3].set_volume(0.1)
    else:
        player_sound[3].stop()

    if c_key and plane or c_key and plane and iswalkl or c_key and plane and iswalkr or c_key and fly_ or c_key and iswalkl and fly_ or c_key and iswalkr and fly_:
        if j < 11:
            player_sound[6].play()
            player_sound[6].set_volume(.1)
    else:
        player_sound[6].stop()

    if d_key and plane or d_key and plane and iswalkl or d_key and plane and iswalkr or d_key and downkey or d_key and iswalkl and downkey or d_key and iswalkr and downkey:
        if j < 11:
            player_sound[7].play()
            player_sound[7].set_volume(.1)
    else:
        player_sound[7].stop()

    for index in range(num_of_bullets):
        continues_bullet(index)


def jarvis_help():
    global jarvis
    if beam_help:
        jarvis = pygame.transform.scale(jarvis, (100, 100))
        cen = jarvis.get_rect()
        cen.center = (int(width / 2), int(height * .05))
        screen.blit(jarvis, cen)
        type('Power Not Enough', int(width / 2), int(height * .05), 255, 0, 0, 50, True)
        type('Jarvis: Sir, Arc reactor power is not enough for beam', int(width / 2), int(height * .1), 224, 244, 244,
             20, True)
        type(str(5 - beam_var) + ' times shot or attack thanos to recharge arc reactor', int(width / 2),
             int(height * .15), 224, 244, 244, 20, True)


def gameloop():
    # Sound
    mixer.music.load("iron_man_bgm.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.4)

    global playerX, playerY, wimg, wimgchg, down_, domo_, img, img_chg, dshi, shi, shi_chg, fly, fly_chg, fight_img, fight_chg_img, beam_img, beam_chg_img, playerX_change, playerY_change, iswalkl, iswalkr, fly_, plane, downkey, s_key, c_key, f_key, d_key, w_key, game_exit, screen, pause, player_power_attack, choice, player_hitbox, enemy_hitbox, enemy_bulletbox, x, y, z, bg_var, beam_help

    # enemy
    global enemyx, enemyy, s_img, w_img
    while not game_exit:
        clock.tick(18)
        screen.fill((0, 0, 0))
        if int(pl_health / 10) + 20 <= int(en_health / 10):
            bg_var = 2
        elif int(en_health / 10) + 20 <= int(pl_health / 10):
            bg_var = 1
        else:
            bg_var = 0
        screen.blit(pygame.transform.scale(background[bg_var], (width, height)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_LEFT:
                    playerX_change = -14
                    wimgchg = +1
                    iswalkl = True
                if event.key == pygame.K_RIGHT:
                    playerX_change = 14
                    wimgchg = +1
                    iswalkr = True

                if iswalkl and iswalkr:
                    playerX_change = 0

                if event.key == pygame.K_UP:
                    playerY_change = -10
                    fly_chg = +1
                    fly_ = True
                    plane = False
                if event.key == pygame.K_DOWN:
                    fly_ = False
                    downkey = True
                    playerY_change = 40

                if event.key == pygame.K_s:
                    shi_chg = +1
                    s_key = True
                if s_key and iswalkr:
                    playerX_change = 0
                elif s_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_c:
                    fight_chg_img = +1
                    c_key = True
                if c_key and iswalkr:
                    playerX_change = 0
                elif c_key and iswalkl:
                    playerX_change = 0
                elif c_key and fly_:
                    playerY_change = 0
                elif not c_key and fly_:
                    playerY_change = -10

                if event.key == pygame.K_e:
                    fight_chg_img = +1
                    f_key = True
                if f_key and iswalkr:
                    playerX_change = 0
                elif f_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_d:
                    fight_chg_img = +1
                    d_key = True
                if d_key and iswalkr:
                    playerX_change = 0
                elif d_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_w:
                    beam_chg_img = +1
                    if beam_var >= 5:
                        w_key = True
                    elif beam_var < 5:
                        beam_help = True
                if w_key and iswalkr:
                    playerX_change = 0
                elif w_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()

                if en_health <= 0 or pl_health <= 0:
                    playerX_change = 0
                    playerY_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerX_change = 0
                    iswalkl = False
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0
                    iswalkr = False

                if iswalkl and not iswalkr:
                    playerX_change = -14
                if not iswalkl and iswalkr:
                    playerX_change = 14

                if event.key == pygame.K_UP:
                    fly_ = False
                    playerY_change = 20
                if event.key == pygame.K_DOWN:
                    downkey = False
                    playerY_change = 20

                if event.key == pygame.K_s:
                    shi_chg = -10
                    s_key = False
                    player_power_attack = 'none'
                if s_key and iswalkr:
                    playerX_change = 0
                elif s_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_c:
                    fight_chg_img = -10
                    c_key = False
                if c_key and iswalkr:
                    playerX_change = 0
                elif c_key and fly_:
                    playerY_change = 0
                elif not c_key and fly_:
                    playerY_change = -10

                if event.key == pygame.K_e:
                    fight_chg_img = -10
                    f_key = False
                if f_key and iswalkr:
                    playerX_change = 0
                elif f_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_d:
                    fight_chg_img = -10
                    d_key = False
                if d_key and iswalkr:
                    playerX_change = 0
                elif d_key and iswalkl:
                    playerX_change = 0

                if event.key == pygame.K_w:
                    beam_chg_img = -30
                    w_key = False
                    beam_help = False
                    player_power_attack = 'none'
                if w_key and iswalkr:
                    playerX_change = 0
                elif w_key and iswalkl:
                    playerX_change = 0

        playerX += playerX_change
        playerY += playerY_change
        wimg += wimgchg
        img += 1
        shi += shi_chg
        dshi += shi_chg
        down_ += wimgchg
        domo_ += wimgchg
        fly += fly_chg
        fight_img += fight_chg_img
        beam_img += beam_chg_img

        if beam_img >= 50:
            beam_img = 50
        if beam_img <= 0:
            beam_img = 0
        if fight_img >= 11:
            fight_img = 11
        if fight_img <= 0:
            fight_img = 0
        if dshi >= 11:
            dshi = 5
        if dshi <= 0:
            dshi = 0
        if shi >= 9:
            shi = 3
        if shi <= 0:
            shi = 0
        if domo_ >= 10:
            domo_ = 0
        if down_ >= 8:
            down_ = 0
        if wimg >= 12:
            wimg = 0
        if img >= 11:
            img = 0
        if fly >= 4:
            fly = 0
        if playerY >= height - 120:
            playerY = height - 120
            plane = True
        if playerY <= 0:
            playerY = 0
        if playerX <= 0:
            playerX = 0
        elif playerX >= width - 105:
            playerX = width - 105

        if ischoice:
            if player_hitbox[1] + player_hitbox[3] < enemy_hitbox[1]:
                choice = random.choice(['long range teleport', 'walk'])
            elif playerX + 60 + 300 < enemyx or enemyx + 120 + 300 < playerX or enemyx - 300 > playerX + 60 or playerX - 300 > enemyx:
                choice = random.choice(long_range_list)
            else:
                choice = random.choice(combine_list)

        health(int(width * .05), int(height * .05), int(width * .8), int(height * .05))
        jarvis_help()
        enemy(choice, playerX, playerY)
        player(playerX, playerY, img, wimg, fly, down_, domo_, shi, dshi, fight_img, beam_img)
        pygame.display.flip()


intro()
