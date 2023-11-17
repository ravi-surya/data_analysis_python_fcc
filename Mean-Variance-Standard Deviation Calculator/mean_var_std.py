import numpy as np

def calculate(list):
  if len(list) <9:
    raise ValueError('List must contain nine numbers.')

  calculations = {'mean' : '', 'variance' : '', 'standard deviation' : '', 'max' : '', 'min' : '', 'sum' : ''} 
  changed_list= np.array([list[0:3],list[3:6],list[6:9]])
  #flat calculating
  list_flat_mean=changed_list.mean()
  list_flat_max=changed_list.max()
  list_flat_min=changed_list.min()
  list_flat_std=changed_list.std()
  list_flat_var=changed_list.var()
  list_flat_sum=changed_list.sum()
#row or axis=0 calculating
  list_row_mean=changed_list.mean(0)
  list_row_max=changed_list.max(0)
  list_row_min=changed_list.min(0)
  list_row_std=changed_list.std(0)
  list_row_var=changed_list.var(0)
  list_row_sum=changed_list.sum(0)
#column or axis=1 calculating  
  list_col_mean=changed_list.mean(1)
  list_col_max=changed_list.max(1)
  list_col_min=changed_list.min(1)
  list_col_std=changed_list.std(1)
  list_col_var=changed_list.var(1)
  list_col_sum=changed_list.sum(1)

# .tolist() converts numpy arrays to a pyhton lists
  calculations.update({'mean' : [list_row_mean.tolist(),list_col_mean.tolist(),list_flat_mean.tolist()]})
  calculations.update({'max' : [list_row_max.tolist(),list_col_max.tolist(),list_flat_max.tolist()]})
  calculations.update({'min':[list_row_min.tolist(),list_col_min.tolist(),list_flat_min.tolist()]})
  calculations.update({'standard deviation':[list_row_std.tolist(),list_col_std.tolist(),list_flat_std.tolist()]})
  calculations.update({'variance':[list_row_var.tolist(),list_col_var.tolist(),list_flat_var.tolist()]})
  calculations.update({'sum':[list_row_sum.tolist(),list_col_sum.tolist(),list_flat_sum.tolist()]})
  

  return calculations