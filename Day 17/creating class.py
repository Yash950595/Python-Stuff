class User:
    def __init__(self,user_id,username): #here __init__ is the constructor which associates the attributes with objects and creates the objects
                                        # here self is the default parameter
        self.id=user_id 
        self.username=username

        # here .id and .username is the attribute associated with self and user_id and username are the parameters

    
user1=User(20251,"Yash")
user2=User(20252,"Ojas")

print(user1.id)  
print(user2.username)

#We cannot print the object entirely. We can only print the attributes associated with a particular object.
# Print an entire object returns garbage value 