# NetDim
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

import tkinter as tk
from tkinter import ttk
from miscellaneous import FocusTopLevel

class AdvancedGraphOptionsWindow(FocusTopLevel):
    def __init__(self, master):
        super().__init__()
        self.ms = master
        self.title("Advanced graph options")

        ## Shortest path section
        
        # shortest path algorithms include:
        #   - shortest path with A* (Dijkstra)
        #   - shortest path with Bellman-Ford
        #   - shortest path with Floyd-Warshall
        #   - shortest path with Linear programming

        # label frame for shortest path algorithms
        self.lf_sp = ttk.Labelframe(self, padding=(6, 6, 12, 12), 
                                            text='Shortest path algorithms')
        self.lf_sp.grid(row=1, column=0, columnspan=2, pady=5, padx=5, 
                                                                sticky='nsew')

        self.sp_algorithms = {
        "A* algorithm": self.ms.cs.ntw.A_star,
        "Bellman-Ford algorithm": self.ms.cs.ntw.bellman_ford,
        "Floyd-Warshall algorithm": self.ms.cs.ntw.floyd_warshall,
        "Linear programming algorithm": self.ms.cs.ntw.LP_SP_formulation
        }

        # List of shortest path algorithms
        self.sp_list = ttk.Combobox(self, width=9)
        self.sp_list["values"] = tuple(self.sp_algorithms.keys())
        self.sp_list.current(0)
        self.sp_list.grid(in_=self.lf_sp, row=0, column=0,
                                columnspan=2, pady=5, padx=5, sticky="nsew")
                                
        self.sp_src_label = ttk.Label(self, text="Source :")
        self.sp_src_entry = ttk.Entry(self)
        self.sp_src_label.grid(in_=self.lf_sp, row=1, column=0, pady=5, padx=5, sticky=tk.W)
        self.sp_src_entry.grid(in_=self.lf_sp, row=1, column=1, pady=5, padx=5, sticky=tk.W)
        
        self.sp_dest_label = ttk.Label(self, text="Destination :")
        self.sp_dest_entry = ttk.Entry(self)
        self.sp_dest_label.grid(in_=self.lf_sp, row=2, column=0, pady=5, padx=5, sticky=tk.W)
        self.sp_dest_entry.grid(in_=self.lf_sp, row=2, column=1, pady=5, padx=5, sticky=tk.W)
        
        self.bt_sp = ttk.Button(self, text="Compute path", command=self.compute)
        self.bt_sp.grid(in_=self.lf_sp, row=3, column=0, columnspan=2, pady=5, padx=5)
        
        ## Flow section
        
        # flow algorithms include:
        #   - maximum flow with Ford-Fulkerson
        #   - maximum flow with Edmond-Karps
        #   - maximum flow with Dinic
        #   - maximum flow with Linear programming
        #   - minimum-cost flow with Linear programming
        #   - minimum-cost flow with Klein (cycle-cancelling algorithm)
        
        # label frame for shortest path algorithms
        self.lf_flow = ttk.Labelframe(self, padding=(6, 6, 12, 12), 
                                            text='Flow algorithms')
        self.lf_flow.grid(row=1, column=2, columnspan=2, pady=5, padx=5, 
                                                                sticky='nsew')
                                                                
        self.flow_algorithms = {
        "Ford-Fulkerson (MF)": self.ms.cs.ntw.ford_fulkerson,
        "Edmond-Karps (MF)": self.ms.cs.ntw.edmonds_karp,
        "Dinic (MF)": self.ms.cs.ntw.dinic,
        "Linear programming (MF)": self.ms.cs.ntw.LP_MF_formulation,
        "Linear programming (MCF)": self.ms.cs.ntw.LP_MCF_formulation,
        "Klein (MCF)": lambda: "to be implemented"
        }
        
        # List of flow path algorithms
        self.flow_list = ttk.Combobox(self, width=9)
        self.flow_list["values"] = tuple(self.flow_algorithms.keys())
        self.flow_list.current(0)
        self.flow_list.grid(in_=self.lf_flow, row=0, column=0,
                                columnspan=2, pady=5, padx=5, sticky="nsew")
                                
        self.flow_src_label = ttk.Label(self, text="Source :")
        self.flow_src_entry = ttk.Entry(self)
        self.flow_src_label.grid(in_=self.lf_flow, row=1, column=0, pady=5, padx=5, sticky=tk.W)
        self.flow_src_entry.grid(in_=self.lf_flow, row=1, column=1, pady=5, padx=5, sticky=tk.W)
        
        self.flow_dest_label = ttk.Label(self, text="Destination :")
        self.flow_dest_entry = ttk.Entry(self)
        self.flow_dest_label.grid(in_=self.lf_flow, row=2, column=0, pady=5, padx=5, sticky=tk.W)
        self.flow_dest_entry.grid(in_=self.lf_flow, row=2, column=1, pady=5, padx=5, sticky=tk.W)
        
        self.bt_flow = ttk.Button(self, text="Compute flow", command=self.compute)
        self.bt_flow.grid(in_=self.lf_flow, row=3, column=0, columnspan=2, pady=5, padx=5)
        
        # hide the window when closed
        self.protocol("WM_DELETE_WINDOW", self.withdraw)
        self.withdraw()
                                        
    def compute(self):
        source = self.ms.cs.ntw.nf(name=self.sp_src_entry.get())
        destination = self.ms.cs.ntw.nf(name=self.sp_dest_entry.get())
        print(self.sp_algorithms[self.sp_list.get()](source, destination))
        
    #     # Label for the name/type of the AS
    #     self.label_source = tk.Label(self, bg="#A1DBCD", text="Source")
    #     self.label_destination = tk.Label(self, bg="#A1DBCD", text="Destination")
    #     
    #     # Entry box for the name of the AS
    #     self.entry_source = tk.Entry(self, textvariable="node1", width=10)
    #     self.entry_destination = tk.Entry(self, textvariable="node4", width=10)
    #     
    #     # flow for minimum cost flow
    #     self.label_flow = tk.Label(self, bg="#A1DBCD", text="Flow")
    #     self.entry_flow = tk.Entry(self, textvariable="12", width=10)
    #     
    #     # selection des paths par l'utilisateur
    #     self.button_create_hypercube = ttk.Button(self, text='Create hypercube', command = lambda: self.add_nodes(master))
    #     self.button_create_square_tiling = ttk.Button(self, text='Create square tiling', command = lambda: master.cs.ntw.generate_square_tiling(100, "router"))
    #     self.button_highlight_connected_components = ttk.Button(self, text='Highlight connected components', command = lambda: self.highlight_connected_components(master))
    #     self.button_LP = ttk.Button(self, text='LP', command = lambda: self.LP_SP(master))
    #     self.button_LP_MF = ttk.Button(self, text='LP MF', command = lambda: self.LP_MF(master))
    #     self.button_fulkerson = ttk.Button(self, text='Fulkerson', command = lambda: self.fulkerson(master))
    #     self.button_kruskal = ttk.Button(self, text='Minimum spanning tree', command = lambda: self.kruskal(master))
    #     self.button_mcf = ttk.Button(self, text='Minimum cost flow', command = lambda: self.LP_MCF(master))
    #     self.button_lpldsp = ttk.Button(self, text='LP LDSP', command = lambda: self.LP_LDSP(master))
    #     self.button_bhandari = ttk.Button(self, text='Bhandari', command = lambda: self.bhandari(master))
    #     self.button_suurbale = ttk.Button(self, text='Suurbale', command = lambda: self.suurbale(master))
    #     self.button_spt = ttk.Button(self, text='SPT', command = lambda: self.dijkstra_tree(master))
    #     
    #     # affichage des buttons / label dans la grille
    #     self.button_create_hypercube.grid(row=1,column=0, pady=5, padx=5, sticky=tk.W)
    #     self.button_create_square_tiling.grid(row=1,column=1, pady=5, padx=5, sticky=tk.W)
    #     self.button_highlight_connected_components.grid(row=2,column=3, pady=5, padx=5, sticky=tk.W)
    #     self.button_LP.grid(row=2,column=0, pady=5, padx=5, sticky=tk.W)
    #     self.button_fulkerson.grid(row=2,column=1, pady=5, padx=5, sticky=tk.W)
    #     self.button_kruskal.grid(row=5,column=1, pady=5, padx=5, sticky=tk.W)
    #     self.button_mcf.grid(row=7,column=1, pady=5, padx=5, sticky=tk.W)
    #     self.button_bhandari.grid(row=7,column=2, pady=5, padx=5, sticky=tk.W)
    #     self.button_suurbale.grid(row=8,column=2, pady=5, padx=5, sticky=tk.W)
    #     self.button_spt.grid(row=9,column=2, pady=5, padx=5, sticky=tk.W)
    #     self.button_lpldsp.grid(row=10,column=2, pady=5, padx=5, sticky=tk.W)
    #     self.button_LP_MF.grid(row=11,column=2, pady=5, padx=5, sticky=tk.W)
    #     
    #     self.label_source.grid(row=3,column=0, pady=5, padx=5, sticky=tk.W)
    #     self.label_destination.grid(row=4,column=0, pady=5, padx=5, sticky=tk.W)
    #     self.entry_source.grid(row=3,column=1, pady=5, padx=5, sticky=tk.W)
    #     self.entry_destination.grid(row=4,column=1, pady=5, padx=5, sticky=tk.W)
    #     
    #     self.label_flow.grid(row=6, column=0, pady=5, padx=5, sticky=tk.W)
    #     self.entry_flow.grid(row=6, column=1, pady=5, padx=5, sticky=tk.W)
    #     
    #     # hide the window when closed
    #     self.protocol("WM_DELETE_WINDOW", self.withdraw)
    #     self.withdraw()
    #     
    # def highlight_connected_components(self, master):
    #     master.cs.unhighlight_all()
    #     for idx, connex_comp in enumerate(master.cs.ntw.connected_components()):
    #         for node in connex_comp:
    #             for adjacent_link in master.cs.ntw.graph[node]["trunk"]:
    #                 master.cs.itemconfig(adjacent_link.line, fill=master.cs.default_colors[idx])
    #                 
    # def LP_SP(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     flow = master.cs.ntw.LP_SP_formulation(source, destination)
    #     print(flow)
    #     
    # def LP_MF(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     flow = master.cs.ntw.LP_MF_formulation(source, destination)
    #     print(flow)
    #     
    # def LP_MCF(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     flow = float(self.entry_flow.get())
    #     cost = master.cs.ntw.LP_MCF_formulation(source, destination, flow)
    #     print(cost)
    #     
    # def fulkerson(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     flow = master.cs.ntw.edmonds_karp(source, destination)
    #     print(flow)
    #     
    # def kruskal(self, master):
    #     links_mst = master.cs.ntw.kruskal(master.cs.ntw.pn["node"].values())
    #     master.cs.highlight_objects(*links_mst)
    #     
    # def bhandari(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     spair = master.cs.ntw.bhandari(source, destination)
    #     master.cs.highlight_objects(*spair)
    #     
    # def suurbale(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     spair = master.cs.ntw.suurbale(source, destination)
    #     master.cs.highlight_objects(*spair)
    #     
    # def dijkstra_tree(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     _, _, spt = master.cs.ntw.dijkstra(source, destination)
    #     master.cs.highlight_objects(*spt)
    #     
    # def LP_LDSP(self, master):
    #     source = master.cs.ntw.nf(name=self.entry_source.get())
    #     destination = master.cs.ntw.nf(name=self.entry_destination.get())
    #     K = int(self.entry_flow.get())
    #     somme = master.cs.ntw.LP_LDSP_formulation(source, destination, K)
    #     print(somme)
        
    # def generate_square_tiling(self, scenario):
    #     self.erase_graph(scenario)
    #     scenario.generate_meshed_square(self.var_dimension.get())
    #     
    # def generate_hypercube(self, scenario):
    #     self.erase_graph(scenario)
    #     scenario.generate_hypercube(self.var_dimension.get())
    #     
        
    # TODO K-shortest path with BFS
        # _, source, *e = self.get_user_input(master)
        # print(source)
        # for p in master.cs.ntw.all_paths(source):
        #     print(p)
        
    # TODO flow window
    # def flow(self, master):
    #     total_flow = master.cs.ntw.ford_fulkerson(master.cs.ntw.nf(self.entry_source_node.get()), master.cs.ntw.nf(self.entry_destination_node.get()))
    #     self.var_total_flow.set(str(total_flow))
        
        
                    