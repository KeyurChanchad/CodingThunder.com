
from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("My GUI With Keyur")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# borderwidth
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
# image

title_label = Label(text ='''
Lucifer is an American urban fantasy superhero television series developed by Tom Kapinos that premiered on Fox on January 25, 2016.\n It is based on the DC Comics character created by Neil Gaiman, Sam Kieth, and Mike Dringenberg taken from the comic book series\n The Sandman, who later became the protagonist of a spin-off comic book series, both published by DC Comics' Vertigo imprint.\n The series is produced by Jerry Bruckheimer Television, DC Entertainment and Warner Bros.\n TelevisionThe series revolves around the story of Lucifer Morningstar (Tom Ellis),\n the Devil, who abandons Hell for Los Angeles where he runs his own nightclub named Lux and becomes a consultant to the Los Angeles Police Department (LAPD).\n The ensemble and supporting cast include Lauren German as Detective Chloe Decker,\n Kevin Alejandro as Detective Daniel "Dan" Espinoza, D. B. Woodside as Amenadiel, Lesley-Ann Brandt as Mazikeen,\n Rachael Harris as Dr. Linda Martin, and (beginning in season 2) Aimee Garcia as Ella Lopez.\n Filming took place primarily in Vancouver, British Columbia, before production was relocated entirely to Los Angeles, California, beginning with the third season.''', bg = "blue" , fg="white", padx=13, pady=94, font="comicsansms 14 bold", relief = GROOVE, borderwidth=3)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# anchor = 'sw' is not do in south west side for that we write side = Bottom
# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


