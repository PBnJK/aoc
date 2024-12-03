# Day 2: Red-Nosed Reports

include("util.jl")

using .Util

lines = Util.getinput("day02.txt")

checksorted(d) = (issorted(d) || issorted(d, rev=true))
checkdiff(d) = all(y->abs(y) ∈ 1:3, diff(d))

allok(d) = checksorted(d) && checkdiff(d)
function star1()
	total = 0
	for d ∈ lines
		d = parse.(Int64, split(d))
		if allok(d)
			total += 1
		end
	end

	println("- $total")
end

function star2()
	total = 0
	for d ∈ lines
		d = parse.(Int64, split(d))
		for i ∈ eachindex(d)
			ds = deleteat!(copy(d), i)
			if allok(ds)
				total += 1
				break
			end
		end
	end

	println("- $total")
end

star1()
star2()
