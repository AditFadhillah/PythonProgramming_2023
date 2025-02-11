import exam_re as exam

#Q1
print("\nQ1")
exam.print_lines("lines.txt")
exam.order_numbers("lines.txt")
exam.order_lines("lines.txt")
print()
exam.order_lines_compact("lines.txt")

#Q2
print("\nQ2")
zipcode_dict = exam.read_zipcode_file("zipcodes.dk.csv")
#print(zipcode_dict)
region_hovedstaden_zip_count = exam.count_zipcodes_per_state(zipcode_dict, "Region Hovedstaden")
print(region_hovedstaden_zip_count)
max_distance_zipcode_pair = exam.max_distance(zipcode_dict)
print(max_distance_zipcode_pair)

#Q3
print("\nQ3")
with open("happy_sad.txt") as input:
    for line in input:
        match = exam.happy_sad_re.match(line.rstrip())
        print(match.group(0))
        assert match is not None
assert exam.happy_sad_re.match(":-[") is None

with open("happy_sad.txt") as input:
    for line in input:
        match = exam.happy_sad_re2.match(line.rstrip())
        print("eyes: ", match.group(1), "\tmouth: ", match.group(2))
        assert match is not None
print("Find happy:")
exam.find_happy(":( :( :(\n:) :( :( :( ;)\n:-( (bla bla bla) :)")
print(exam.make_string_happy(":( :( :(\n:) :( :( :( ;)\n:-( (bla bla bla) :)"))

#Q4
print("\nQ4")
smiley_image_array = exam.read_image_array('smiley_text_image.txt')
smiley_image_array_labels = exam.read_image_array('smiley_text_image_labels.txt')
print(repr(smiley_image_array))
print(repr(smiley_image_array_labels))

print(repr(exam.change_image_array_foreground(smiley_image_array, 'X')))
print(repr(exam.frame_image_array(smiley_image_array, frame_width=2)))
print(repr(exam.make_image_array_happy(smiley_image_array, smiley_image_array_labels)))

#Q5
print("\nQ5")
mnist_collection = exam.MnistCollection("mnist_test_200.csv")
print(mnist_collection.data)

images_of_seven = mnist_collection.get_images_for_digit(digit=7)
images_of_seven_first = images_of_seven[0]
print(repr(images_of_seven_first))
print(exam.mnist_pretty_print(images_of_seven_first))

print(repr(mnist_collection.get_slimmest_image_for_digit(digit=7)))
print(exam.mnist_pretty_print(mnist_collection.get_slimmest_image_for_digit(digit=7)))

