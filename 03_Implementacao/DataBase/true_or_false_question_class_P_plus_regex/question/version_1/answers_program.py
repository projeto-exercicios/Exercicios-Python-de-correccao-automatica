answer_1_true = regular_search("2", e)
new_b = regular_subtitution("1", "2", e)
answer_2_true = regular_search("2", new_b) / answer_1_true
answer_3_true = o[1].num
new_new_b = regular_subtitution("[^2]", "2", new_b)
answer_4_true = regular_search("2", new_new_b) 
answer_5_true = power(o[1].num, 2)
print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
