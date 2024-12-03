# Day 3: Mull It Over

include("util.jl")

using .Util

prog = Util.getinputn("day03.txt")

function star1()
	total = 0
	for m ∈ eachmatch(r"mul\((\d{1,3}),(\d{1,3})\)", prog)
		total += parse(Int64, m[1]) * parse(Int64, m[2])
	end

	println("- $total")
end

function star2()
	on = true

	total = 0
	for m ∈ eachmatch(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", prog)
		if m.match == "do()"
			on = true
		elseif m.match == "don't()"
			on = false
		elseif on
			total += parse(Int64, m[1]) * parse(Int64, m[2])
		end
	end

	println("- $total")
end

star1()
star2()
