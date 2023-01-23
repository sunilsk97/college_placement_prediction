import numpy as np  
import json
import pickle
import config


class CollegePlacement():
    def __init__(self,Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs):
        self.Age = Age
        self.Gender = Gender
        self.Stream = Stream
        self.Internships = Internships
        self.CGPA = CGPA
        self.Hostel = Hostel
        self.HistoryOfBacklogs = HistoryOfBacklogs

    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_placed_not(self):
        self.load_model()


        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.Age
        test_array[1] = self.json_data["Gender"][self.Gender]
        test_array[2] = self.json_data["Stream"][self.Stream]
        test_array[3] = self.Internships
        test_array[4] = self.CGPA
        test_array[5] = self.Hostel
        test_array[6] = self.HistoryOfBacklogs

        print("test_array:",test_array) # 7 values

        placedorno = self.model.predict([test_array])[0]
        return placedorno


if __name__ == "__main__":

    Age  = 19
    Gender = 'Male'
    Stream = 'Civil'
    Internships  = 1
    CGPA  = 8
    Hostel = 0
    HistoryOfBacklogs = 1

    clg_place = CollegePlacement(Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs)
    clg_place.get_placed_not()