# Day 5: Print Queue

include("util.jl")

using .Util
using DataStructures: DefaultDict

r, p = split.(strip.(split(Util.getinputn("day05.txt"), "\n\n")), "\n")
rules = DefaultDict(Set)
for rule ∈ r
	f, t = split(rule, "|")
	push!(rules[f], t)
end


function star1()
	valid = []
	for pages ∈ p
		visited = Set()
        good = true

		pages = split(pages, ",")
        for page ∈ pages
			if !isdisjoint(rules[page], visited)
                good = false
                break
			end

            push!(visited, page)
		end

		if good push!(valid, pages) end
	end

	total = sum(parse(Int64, x[length(x) ÷ 2 + 1]) for x ∈ valid)
	println("- $total")
end

function star2()
	invalid = []
	for pages ∈ p
		visited = Set()
        bad = false

		pages = split(pages, ",")
        for page ∈ pages
			if !isdisjoint(rules[page], visited)
                bad = true
                break
			end

            push!(visited, page)
		end

		if bad push!(invalid, pages) end
	end

	for v ∈ invalid
        swaps = 0
        while true
			for i=1:length(v)-1
                if v[i] ∈ rules[v[i + 1]]
                    v[i], v[i + 1] = v[i + 1], v[i]
                    swaps += 1
				end
			end

            if swaps == 0
                break
			end

            swaps = 0
		end
	end

	total = sum(parse(Int64, x[length(x) ÷ 2 + 1]) for x ∈ invalid)
	println("- $total")
end

star1()
star2()

