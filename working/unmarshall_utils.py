

def  create_array (input_str:str, idx:int):
    cur_list = []
    try:
        alpha=input_str[idx]
        if alpha == "[":
            output_list = create_array(input_str, idx + 1)
            return output_list
        elif alpha == "]":
            return cur_list
        elif alpha  in [",", " ", "\'"]:
            output_list = create_array(input_str, idx + 1)
            return output_list

        else:
            output_list = create_array(input_str, idx + 1)
            output_list.insert(0, alpha)
            return output_list
    except IndexError:
        return cur_list

if  __name__ ==  "__main__":
    simple_array=[1,[2,3],4]
    print(create_array(simple_array.__repr__(),0))