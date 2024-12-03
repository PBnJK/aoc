# Day 1: Historian Hysteria

include("util.jl")

using .Util

lines = Util.getinput("day01.txt")

function star1()
	id1 = []
	id2 = []

	for line ∈ lines
		if line == ""
			break
		end

		a, b = split(line, "   ")
		push!(id1, parse(Int64, a))
		push!(id2, parse(Int64, b))
	end

	id1 = sort(id1)
	id2 = sort(id2)

	result = sum([abs(x - y) for (x, y) ∈ zip(id1, id2)])
	println("- $result")
end

function star2()
	llist = []
	summap = Dict()

	for line ∈ lines
		if line == ""
			break
		end

		a, b = split(line, "   ")
		
		a = parse(Int64, a)
		push!(llist, a)

		b = parse(Int64, b)
		if !haskey(summap, b)
			summap[b] = 1
		else
			summap[b] += 1
		end
	end

	result = sum([(n * get(summap, n, 0)) for n ∈ llist])
	println("- $result")
end

star1()
star2()
