#access the value of key history


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
History = sample_dict["class"]["student"]["marks"]["history"]
print(History)
