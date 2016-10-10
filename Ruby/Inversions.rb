#!/usr/bin/ruby

# Counting inversions for algo class

# First method is recursive. We just divide up the array and call merge subroutine

def divide(input)
        # Base case
	if input.length <= 1
		return [0, input]
	end
        # Recursion!
	mid = (input.length / 2)
	left = input[0..(mid - 1)] 
	right = input[mid..(input.length - 1)]
	left_result = divide(left)
	right_result = divide(right)
	merge_result = conquer(left_result[1], right_result[1])
	return [left_result[0] + right_result[0] + merge_result[0], merge_result[1]]
end

# Here is where we do the real work. We iterate over both arrays
# and mark places where left array is bigger than right. We return
# An array with a number of inversions.

def conquer(left, right)
	arr = []
	i = 0
        j = 0
	inv = 0
	while i < left.length and j < right.length
		if left[i] < right[j]
			arr << left[i]
			i+=1
		else
			arr << right[j]
			j+=1
			inv = inv + left.length - i
		end
	end
	if i < left.length
		arr += left[i..(left.length - 1)]
	else
		arr += right[j..(right.length - 1)]
	end
	return [inv, arr]
end

count_file = ARGV[0]
f = File.open(count_file)
test = f.readlines()
test = test.map(&:to_i)
final = divide(test)
puts "How many inversions? This many: " + final[0].to_s
