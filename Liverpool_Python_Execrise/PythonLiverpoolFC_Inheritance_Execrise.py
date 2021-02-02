class LiverpoolFC:
    def __init__(self,name,MaleDefenders = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Male_Defenders.csv"),  MaleForwards = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Male_Forwards.csv"),  MaleMidfielders = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Male_Midfielders.csv"), MaleGoalkeepers = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Male_Goalkeepers.csv"),Male_TeamStaff = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Male_TeamStaff.csv")   ):
                                 
        self.name = name
        self.MaleDefenders = MaleDefenders
        self.MaleMidfielders = MaleMidfielders
        self.MaleForwards = MaleForwards
        self.MaleGoalkeepers = MaleGoalkeepers
        self.Male_TeamStaff = Male_TeamStaff
        
    def MaleMidfielders2020_2021Season(self):
        print((self.MaleMidfielders))
    def MaleForwards2020_2021Season(self):
        print(self.MaleForwards)
    def ClubMotto(self):
        print("You'll never walk alone!")
    def ClubDirectors(self):
        print({'J.Henry': '(Principal Owner)Director','T. Werner':'Director','M.Gordon':'Director','B. Horgan':'(Chief Executive Officer)Director', 'M.Egan':'Director', 'K. Dalglish':'Director','A. Hughes':'Director'})
     
    def ClubColors2020_2021Season(self):
        print({'Home':'Red', 'Away':'Black'})
    
    def MaleTeamStaff2020_2021Season(self):
        print(self.Male_TeamStaff())
        
    def MaleTeam_HighestGoalScorer(self):
        print({'Mohammed_Salah':'15 Goals'})
    

    
class LiverpoolLadiesFC(LiverpoolFC):
    def __init__(self, name,FemaleDefenders = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Female_Defenders.csv"),FemaleForwards = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Female_Forwards.csv"), FemaleMidfielders = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Female_Midfielders.csv"), FemaleGoalkeepers = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Female_Goalkeepers.csv"),Female_TeamStaff = pd.read_csv("/home/nosa2k/Documents/Liverpool_Python_Execrise/Male_TeamStaff.csv") ):
        super().__init__(self,name)
        self.name = name
        self.FemaleDefenders = FemaleDefenders
        self.FemaleMidfielders = FemaleMidfielders
        self.FemaleForwards = FemaleForwards
        self.FemaleGoalkeepers = FemaleGoalkeepers
        self.Female_TeamStaff = Female_TeamStaff
           
    def FemaleMidfielders2020_2021Season(self):
            print((self.FemaleMidfielders))
        
    def FemaleForwards2020_2021Season(self):
            print(self.FemaleForwards)
             
    def HighestFemaleGoalScorer2020_2021Season(self):
            print({'Amalie_Thestrup': '15 Goals','Rinsola_Babajide': '15 Goals','Melissa_Lawley':'15 Goals', 'Taylor_Hinds': '15 Goals'} )
               
    def FemaleTeamStaff2020_2021Season(self):
            print(self.Female_TeamStaff())
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
        
    Ladies = LiverpoolLadiesFC(name = "LiverpoolLadies")
    Ladies.ClubDirectors()
