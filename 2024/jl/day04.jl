# Day 4: Ceres Search

include("util.jl")

using .Util

ws = Util.getinput("day04.txt")

get(a, i, default='.') = try a[i] catch; default end
getws(x, y, default='.') = try get(ws[x], y) catch; default end

function checkhorz(i, j)
	total = 0
	if getws(i, j+1) == 'M' && getws(i, j+2) == 'A' && getws(i, j+3) == 'S'
		total += 1
	end

	if getws(i, j-1) == 'M' && getws(i, j-2) == 'A' && getws(i, j-3) == 'S'
		total += 1
	end
	
	return total
end

function checkvert(i, j)
	total = 0
	if getws(i+1, j) == 'M' && getws(i+2, j) == 'A' && getws(i+3, j) == 'S'
		total += 1
	end

	if getws(i-1, j) == 'M' && getws(i-2, j) == 'A' && getws(i-3, j) == 'S'
		total += 1
	end
	
	return total
end

function checkdiag(i, j)
	total = 0
	if getws(i+1, j+1) == 'M' && getws(i+2, j+2) == 'A' && getws(i+3, j+3) == 'S'
		total += 1
	end

	if getws(i+1, j-1) == 'M' && getws(i+2, j-2) == 'A' && getws(i+3, j-3) == 'S'
		total += 1
	end

	if getws(i-1, j+1) == 'M' && getws(i-2, j+2) == 'A' && getws(i-3, j+3) == 'S'
		total += 1
	end
	
	if getws(i-1, j-1) == 'M' && getws(i-2, j-2) == 'A' && getws(i-3, j-3) == 'S'
		total += 1
	end

	return total
end

function check(i, j)
	return checkhorz(i, j) + checkvert(i, j) + checkdiag(i, j)
end

function star1()
	total = 0
	for (i, line) ∈ enumerate(ws)
		for (j, c) ∈ enumerate(line)
			if c != 'X'
				continue
			end

			total += check(i, j)
		end
	end

	println("- $total")
end

checkmas(l1, l2, l3) = Int(get(l2, 1) == 'A' && (get((l1, 0) == 'M' && get(l3, 2) == 'S') or (get(l1, 0) == 'S' && get(l3, 2) == 'M')) && ((l1[2] == 'M' && l3[0] == 'S') or (l1[2] == 'S' && l3[0] == 'M')))

function star2()
	total = 0
	for i ∈ eachindex(ws)
		for j ∈ eachindex(ws[i])
			total += checkmas(ws[i][j:j+3],ws[i+1][j:j+3],ws[i+2][j:j+3])
		end
	end

	println("- $total")
end

star1()
star2()


