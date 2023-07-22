items_list=[
       {'name':'apple','category':'fruits'},
       {'name':'carrot','category':'vegtables'},
       {'name':'banana','category':'fruits'},
       {'name':'broccoli','category':'vegtables'}]

fruit=[]   
vegtable=[]
  

for item in items_list:
       if (item['category']=='fruits'):
              fruit.append(item['name'])
       if (item['category']=='vegtables'):
              vegtable.append(item['name'])
print("fruits:",fruit)
print("vegtables:",vegtable)
category={
       "fruits":fruit,
       "vegtables":vegtable
}    
print(category)