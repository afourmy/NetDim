# NetDim (contact@netdim.fr)

import tkinter as tk
from graph_generation.multiple_objects import MultipleNodes
from miscellaneous.decorators import update_paths
from pythonic_tkinter.preconfigured_widgets import Menu

class NetworkGeneralRightClickMenu(Menu):
    
    @update_paths
    def __init__(self, event, controller):
        super().__init__()

        x, y = self.view.cvs.canvasx(event.x), self.view.cvs.canvasy(event.y)
        
        # change geographical projection
        projection_menu = tk.Menu(self, tearoff=0)

        projection_menu.add_command(
                label = 'Linear projection', 
                command= lambda: self.view.change_projection('linear')
                )
        projection_menu.add_command(
                label = 'Mercator projection', 
                command= lambda: self.view.change_projection('mercator')
                )
        projection_menu.add_command(
                label = 'Spherical projection', 
                command= lambda: self.view.change_projection('globe')
                )

        self.add_cascade(label='Geographical projection', menu=projection_menu)
        
        # multiple nodes creation
        self.add_command(label='Create multiple nodes', 
                command=lambda: MultipleNodes(x, y, self.controller))
                
        # remove all failures if there is at least one
        if self.network.failed_obj:
            self.add_command(label='Remove all failures',
                    command=lambda: self.remove_all_failures())
            self.add_separator()
                   
        # find networks
        self.add_command(label='Refresh', 
                command=lambda: self.refresh())
                
        # make the menu appear    
        self.tk_popup(event.x_root, event.y_root)

    def remove_all_failures(self):
        self.view.remove_failures()
        self.destroy()
        
    def refresh(self):
        self.project.refresh()
        self.destroy()