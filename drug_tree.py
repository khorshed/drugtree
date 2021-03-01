# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:24:53 2021

@author: Khorshed
"""
class DrugTree():
    def __init__(self, name = "root", childern = None):
        self.name = name
        self.children = []
        
        if childern is not None:
            for child in childern:
                self.add_child(child)
    
    def __repr__(self):      
        
        
        return 'self.name'
    
    def add_child(self, node):
        self.children.append(node)
    
    def has_children(self, node):
        if node == None:
            return False        
        return True if len(node.children) > 0 else False
        
    def get_node(self,curr_node, curr_elm):
              
        if curr_node == None:
            return None
            
        for child in curr_node.children:  
            if child.name == curr_elm:
                return child
            self.get_node(child,curr_elm)
    
    def print_me(self, node, parent = None):
        # breakpoint()
        
        if node == None :
            return
        
            
        for node in node.children:            
            if parent == None:
                print('-' + node.name)
            else:
                if parent != node.name and len(node.children) > 0:
                    print('--' + node.name)  
                else:
                    print('---' + node.name)    
            self.print_me(node, node.name)
            
           
           
    


'''                                                         Medication
                                                             |
                                                             |
        ---------------------------------------------------------------------------------- -------------------------------                          
        |                                                                                                           |
        |                                                                                                           |
        Cold                                                                                                    Allergy
          |                                                                                                         |
          |
------------------------------------------------------------------                                                  |
       |                                                        |                                   -----------------------------------
Acetaminophen                                                                                       |                       |
-------------------------------                               Dextromethorphan                     Montelukast          Fluticasone   
    |                       |                                   |                                       |                |       |   
Sudafed PE Cold & Cough  Vicks Nyquil D Cold and Flu         Sudafed PE Cold & Cough                 Monus-4         Aller-Pro  Flonase

'''

def pupulate_tree(drglist):
    
    treatment = ''    
    brand = ''   
    
    # breakpoint()
    for dl in drglist:
        drgs = dl.split('/')
        treatment = drgs[1] # assuming 2nd element is always be the Treatent(Cold, Allergy) - first one is empty
        brand = drgs[len(drgs)-1] # assuming last element is always be the Brand (Monus-4, Coricidin HBP Cold & Flu)
        nodes = None
        node = t.get_node(t, treatment)
        
        if node == None:            
            nodes = DrugTree(treatment) 
            t.add_child(nodes)
        else:
            nodes = node
            
        for i, gen in enumerate(drgs[2:len(drgs)-1]): # Skipping 2nd the Last one / Traverse only generics (Acetaminophen, Fluticasone)
            node = t.get_node(nodes, gen)
            if node == None:                
                nodes.add_child(DrugTree(gen, [DrugTree(brand)]))
            else:
                node.add_child(DrugTree(brand))
            
         
if __name__ == '__main__':      

    drugs = ['/Cold/Acetaminophen/Dextromethorphan/Sudafed PE Cold & Cough',
         '/Allergy/Montelukast/Monus-4',
         '/Cold/Acetaminophen/Vicks Nyquil D Cold and Flu', 
         '/Cold/Acetaminophen/Chlorpheniramine Systemic/Coricidin HBP Cold & Flu',         
         '/Allergy/Fluticasone/Aller-Pro',
         '/Allergy/Fluticasone/Flonase' 
        ]
    t = DrugTree('Medication')
    pupulate_tree(drugs)
    print('Medication')
    t.print_me(t)
    
    '''---- OUTPUT ----
    Cold
    --Acetaminophen
    ---Sudafed PE Cold & Cough
    ---Vicks Nyquil D Cold and Flu
    ---Coricidin HBP Cold & Flu
    --Dextromethorphan
    ---Sudafed PE Cold & Cough
    --Chlorpheniramine Systemic
    ---Coricidin HBP Cold & Flu
    Allergy
    --Montelukast
    ---Monus-4
    --Fluticasone
    ---Aller-Pro
    ---Flonase
    '''











