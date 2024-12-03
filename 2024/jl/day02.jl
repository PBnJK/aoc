# Day 2: Red-Nosed Reports

include("util.jl")

using .Util

lines = Util.getinput("day02.txt")

checksorted(d) = (issorted(d) || issorted(d, rev=true))
checkdiff(d) = all(y->abs(y) ∈ 1:3, diff(d))

allok(d) = checksorted(d) && checkdiff(d)
function star1()
	sum = 0
	for d ∈ lines
		d = parse.(Int64, split(d))
		if allok(d)
			sum += 1
		end
	end

	println("- $sum")
end

function star2()
	sum = 0
	for d ∈ lines
		d = parse.(Int64, split(d))
		for i ∈ eachindex(d)
			ds = deleteat!(copy(d), i)
			if allok(ds)
				sum += 1
				break
			end
		end
	end

	println("- $sum")
end

star1()
star2()
