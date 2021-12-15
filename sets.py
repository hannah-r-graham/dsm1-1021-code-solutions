trail_mix = {
"m&ms",
"peanuts",
"raisins",
}

print(trail_mix)

print("cashews" in trail_mix)

print("peanuts" in trail_mix)

trail_mix.add("pretzels")

list=["peanuts", "banana chips", "bits of jerky"]
trail_mix.update(list)

print(trail_mix)

#12
trail_mix.remove("m&ms")

trail_mix.discard("raisins")

trail_mix.discard("rat_poison")
print(trail_mix)

nuts = {

"peanuts",
"cashews",
"almonds",
"walnuts",
"pecans"
}

z = trail_mix.union(nuts)
print("All things that are in both", z)

z= trail_mix.intersection(nuts)
print("the set of all nuts that ARE in trail mix", z)

z= trail_mix.difference(nuts)
print("the set of trail mix that are not in nuts", z)

z=nuts.difference(trail_mix)
print("set of nuts not in trail mix", z)