#!/usr/bin/bash
import argparse

from highway.HighwayProblem.highwayProblem import HighwayProblem
from highway.model.Model import Model
from highway.visualization import show_model


def main():
    parser = argparse.ArgumentParser(description='Highway system')
    parser.add_argument('cities', type=str, help='filename with cities positions')
    parser.add_argument('k', type=int, help='number of highway points')
    parser.add_argument('d', type=float, help='minimal distance between exits')

    args = parser.parse_args()

    cities = Model.parse_file_with_cities(args.cities)
    model = Model(cities, args.k, args.d)

    model.randomize()
    print(model)
    show_model(model)
    hp = HighwayProblem(model)
    hp.steps = 5
    hp.Tmax = 12000.0
    hp.Tmin = 2.5
    state, e = hp.anneal()

    print()
    print(e)
    show_model(model)


if __name__ == '__main__':
    main()
