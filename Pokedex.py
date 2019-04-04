#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import time
import pickle
from bs4 import BeautifulSoup
import requests
import os.path
from PIL import Image, ImageTk, ImageDraw, ImageFont
class attendance_calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")
        self.parent=parent
        self.initUI()
    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        s = ttk.Style()
        s.theme_use('default')
        s.configure("green.Horizontal.TProgressbar", font="calibri 12", foreground='green', background='green',text="asdsdfs")
        Label(self, text="POKEDEX", fg="white", font="calibri 30", bg="red").grid(row=0, column=2)
        Canvas(self, height=4, highlightthickness=0, bg="black").grid(row=1, column=0, columnspan=4)
        self.fetch_button=Button(self, text="Fetch Pokemon"+"\n"+"Data", font="calibri 10",bg="yellow", width=11, command=self.crawler).grid(row=2, column=1, pady=5)

        self.progress = ttk.Progressbar(self,style="green.Horizontal.TProgressbar", orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.grid(row=2, column=2)

        Canvas(self, height=4, highlightthickness=0, bg="black", ).grid(row=3, column=0, columnspan=5)
        Label(self, text="Searching&Filtering", font="calibri 15 bold", fg="black", bg="red").grid(row=4, column=2)
        self.search_entry=Entry(self, font="calibri 11 bold",  width=30)
        self.search_entry.grid(row=5, column=2, pady=7)
        Label(self, text="Filter by type", font="calibri 13",fg="black", bg="red").grid(row=6, column=1)
        self.filter_combobox=ttk.Combobox(self, width=30)
        self.filter_combobox.grid(row=7, column=2, padx=20)
        self.search_button=Button(self, text="SEARCH", font="calibri 12", bg="yellow",command=self.search_data).grid(row=7, column=3)
        Canvas(self, height=4,highlightthickness=0, bg="black").grid(row=8, column=0, columnspan=4, pady=10)
        self.result_label=Label(self, text="Total number of result" , font="calibri 17 bold", fg="black",bg="red")
        self.result_label.grid(row=9,column=2)
        self.result_listbox=Listbox(self, height=15, width=35)
        self.result_listbox.grid(row=10, column=2)
        self.data_button=Button(self, text="Get Pokemon"+"\n"+"Data", font="calibri 12", bg="yellow",command=self.get_pokemon_data).grid(row=10, column=3)
        self.pokemon_frame = Frame(self, height=520, width=450, bg="red")

    def crawler(self):
        self.progress["maximum"] = 100
        try:
            with open('pokemondict.pickle', 'rb') as handle:
                self.nested_data_dict = pickle.load(handle)
            q = 151
            time.sleep(0.05)
            self.progress["value"] = q
            self.progress.update()
            self.color_dict = {"All Types": "", "Normal": "gray", "Grass": "lime green", "Fire": "red",
                               "Water": "dodger blue",
                               "Fighting": "OrangeRed4", "Flying": "cornflower blue", "Poison": "DarkOrchid1",
                               "Ground": "goldenrod", "Rock": "burlywood2", "Bug": "yellow green", "Ghost": "purple1",
                               "Electric": "gold", "Psychic": "hot pink", "Ice": "cyan", "Dragon": "MediumPurple2",
                               "Dark": "saddle brown", "Steel": "gray90", "Fairy": "PaleVioletRed1"}
            self.type_list = ()
            for key in self.color_dict:
                self.type_list += key,
            self.filter_combobox["values"] = sorted(self.type_list)

        except:
            self.color_dict = {"All Types": "", "Normal": "gray", "Grass": "lime green", "Fire": "red",
                               "Water": "dodger blue",
                               "Fighting": "OrangeRed4", "Flying": "cornflower blue", "Poison": "DarkOrchid1",
                               "Ground": "goldenrod", "Rock": "burlywood2", "Bug": "yellow green", "Ghost": "purple1",
                               "Electric": "gold", "Psychic": "hot pink", "Ice": "cyan", "Dragon": "MediumPurple2",
                               "Dark": "saddle brown", "Steel": "gray90", "Fairy": "PaleVioletRed1"}
            self.type_list = ()
            for key in self.color_dict:
                self.type_list += key,
            self.filter_combobox["values"] = sorted(self.type_list)

            f = open("all_pokemon.txt", "r")
            pokemon_names = []
            for x in f:
                x = x.rstrip('\n')
                x = x.lower()
                pokemon_names.append(x)
            linklist = []
            default_link = "https://www.pokemon.com/us/pokedex/"
            for i in range(len(pokemon_names)):
                a = default_link + pokemon_names[i]
                linklist.append(a)
            self.nested_data_dict = {}
            q = 0
            for item in linklist:
                r = requests.get(item)
                data = r.text
                soup = BeautifulSoup(data,"html5lib")

                # Getting name and id
                k = soup.find_all("div", {"class": "pokedex-pokemon-pagination-title"})[0].text
                k = k.replace(" ", "")
                k = k.strip()
                k = k.split("\n")
                if k[0] == "Mr.Mime":
                    k[0] = "Mr. Mime"

                # Getting img url
                k1 = soup.find_all("img")
                for image in k1:
                    if image["alt"] == k[0]:
                        self.img_link = image["src"]
                        break

                # Getting Height
                k2 = soup.find_all("span", {"class": "attribute-value"})[0].text
                k2 = k2.replace(" ", "")

                # Getting Weight
                k3 = soup.find_all("span", {"class": "attribute-value"})[1].text

                # Getting Category
                k4 = soup.find_all("span", {"class": "attribute-value"})[3].text

                # Getting Ability
                k5 = soup.find_all("ul", {"class": "attribute-list"})[0].text
                k5 = k5.split("\n")
                k5list = []
                for i in range(len(k5)):
                    if k5[i] != "":
                        k5list.append(k5[i])

                # Getting Type
                k6 = soup.find_all("div", {"class": "dtm-type"})[0].text
                k6 = k6.split("\n")
                k6list = []
                for i in range(len(k6)):
                    if k6[i] != "Type" and k6[i] != "":
                        k6list.append(k6[i])

                # Getting Weaknesses
                k7 = soup.find_all("div", {"class": "dtm-weaknesses"})[0].text
                k7 = k7.replace("\t", "")
                k7 = k7.replace(" ", "")
                k7 = k7.split("\n")
                k7list = []
                for i in range(len(k7)):
                    if k7[i] != "Weaknesses" and k7[i] != "":
                        k7list.append(k7[i])

                self.nested_data_dict[pokemon_names[q]] = {}
                self.nested_data_dict[pokemon_names[q]]["pokemon_name"] = k[0]
                self.nested_data_dict[pokemon_names[q]]["pokemon_id"] = k[1]
                self.nested_data_dict[pokemon_names[q]]["pokemon_img"] = self.img_link
                self.nested_data_dict[pokemon_names[q]]["pokemon_height"] = k2
                self.nested_data_dict[pokemon_names[q]]["pokemon_weight"] = k3
                self.nested_data_dict[pokemon_names[q]]["pokemon_category"] = k4
                self.nested_data_dict[pokemon_names[q]]["pokemon_ability"] = k5list
                self.nested_data_dict[pokemon_names[q]]["pokemon_type"] = k6list
                self.nested_data_dict[pokemon_names[q]]["pokemon_weakness"] = k7list

                time.sleep(0.05)
                self.progress["value"] = q
                self.progress.update()
                q = q + 1

            with open('pokemondict.pickle', 'wb') as handle:
                pickle.dump(self.nested_data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def search_data(self):
        self.result_listbox.delete(0,END)
        self.pokemon_name=str(self.search_entry.get())
        self.pokemon_list=[]
        if self.pokemon_name=="" and str(self.filter_combobox.get())=="All Types":
            for name in self.nested_data_dict:
                self.pokemon_list.append(name)
            for i in sorted(self.pokemon_list):
                self.result_listbox.insert(END,i.upper())
            self.result_label.destroy()
            Label(self, text="Total: "+str(len(self.pokemon_list))+" Result", font="calibri 17 bold", fg="black", bg="red").grid(row=9,
                                                                                                          column=2)
        elif str(self.filter_combobox.get())=="All Types":
            for name in self.nested_data_dict:
                if self.pokemon_name in name:
                    self.pokemon_list.append(name)
            for i in self.pokemon_list:
                self.result_listbox.insert(END,i.upper())
            self.result_label.destroy()
            Label(self, text="Total: " + str(len(self.pokemon_list))+" Result", font="calibri 17 bold", fg="black",
                  bg="red").grid(row=9,
                                 column=2)
        else:
            selected_type = str(self.filter_combobox.get())
            for name in self.nested_data_dict:
                if self.pokemon_name in name and selected_type in self.nested_data_dict[name]["pokemon_type"]:
                    self.pokemon_list.append(name.upper())
            for i in sorted(self.pokemon_list):
                self.result_listbox.insert(END,i)
            self.result_label.destroy()
            Label(self, text="Total: " + str(len(self.pokemon_list))+" Result", font="calibri 17 bold", fg="black",
                  bg="red").grid(row=9,
                                 column=2)


    def get_pokemon_data(self):
        self.pokemon_frame.destroy()
        self.pokemon_frame=Frame(self, height=520, width=450, bg="red")
        self.pokemon_frame.grid(row=0, column=10, rowspan=20, padx=25, sticky=W)
        sel=self.result_listbox.curselection()
        a=self.result_listbox.get(sel)
        picture=self.img_downloader(a.lower())
        load = Image.open(picture)
        load = load.resize((250, 250), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self.pokemon_frame, image=render, bg="red")
        img.image = render
        img.grid(row=2, column=2)

        for key in self.nested_data_dict:
            if key==a.lower():
                i=3
                for type in self.nested_data_dict[key]["pokemon_type"]:
                    Label(self.pokemon_frame, text=type, font="calibri 12", bg=self.color_dict[type]).grid(row=i, column=2)
                    i+=1
                self.weight=self.nested_data_dict[key]["pokemon_weight"]
                self.category=self.nested_data_dict[key]["pokemon_category"]
                Label(self.pokemon_frame, text=self.result_listbox.get(sel),bg="red", font="calibri 30 bold").grid(row=0, column=2)
                Label(self.pokemon_frame, text=self.nested_data_dict[key]["pokemon_id"],bg="red", font="calibri 20 bold").grid(row=1, column=2)
                Label(self.pokemon_frame, text="Height: "+self.nested_data_dict[key]["pokemon_height"],bg="red", font="calibri 15").grid(row=6, column=2)
                self.abilities=""
                for ability in self.nested_data_dict[key]["pokemon_ability"]:
                    self.abilities+=ability+", "

                self.weakness=""
                for weakness in self.nested_data_dict[key]["pokemon_weakness"]:
                    self.weakness+=weakness+", "

        Label(self.pokemon_frame, text="Abilities: "+self.abilities[:len(self.abilities)-2], bg="red", font="calibri 15").grid(row=9, column=2)
        Label(self.pokemon_frame, text="Weakness: "+self.weakness[:len(self.weakness)-2], bg="red", font="calibri 15").grid(row=10, column=2)
        Label(self.pokemon_frame, text="Weight: "+self.weight, bg="red", font="calibri 15").grid(row=7, column=2)
        Label(self.pokemon_frame, text="Category: "+self.category, bg="red", font="calibri 15").grid(row=8, column=2)

    def img_downloader(self,requested_poke):
        path = r"C:\Users\sumeyyeeminmollaoglu\PycharmProjects\untitled2"

        if os.path.isfile(path + requested_poke + ".png") == True:
            return requested_poke + ".png"
        else:
            img_data = requests.get(self.nested_data_dict[requested_poke]["pokemon_img"]).content
            with open(requested_poke + '.png', 'wb') as handler:
                handler.write(img_data)
            return requested_poke + ".png"



def main():
    root= Tk()
    root.geometry("850x570")
    App = attendance_calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
