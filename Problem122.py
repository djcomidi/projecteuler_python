# http://wwwhomes.uni-bielefeld.de/achim/addition_chain.html
lengths = "0122334344545554556566656666767566767776"
lengths += "7777778677778787888788867787889788888897"
lengths += "8888889898989997888898989998999899999998"
lengths += "999999a78898999899a9aaa8999999a999a9aaa8"
lengths += "999999a9a9a9aaa9aaa9aaa9aaaaaab89999a9a9"
total = sum(int(h, 16) for h in lengths)
print(total)
