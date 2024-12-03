#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <numeric>

/**
 * AOC 2023 Day 8
 * Hans Elliott
 * 
 * Example Input:
 * 
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
 *
*/
typedef std::unordered_map<
    std::string,
    std::vector<std::string>
> network_map;

// split string on delimiter into vector of sub-strings
std::vector<std::string>
stringsplit(std::string str, std::string delim) {
    std::vector<std::string> result;
    std::string sub;
    size_t delimlen = delim.length();

    size_t pos = str.find(delim);
    while (pos != std::string::npos) {
        sub = str.substr(0, pos);
        result.push_back(sub);
        str.erase(0, pos + delimlen); // remove first match from str (+ delim)
        pos = str.find(delim);
    }
    result.push_back(str); // what's left

    return result;
}


/**
 * convert lines defining the network into a hash map where each key
 * is the node and its values are:
 * [next node if direction is left, next node if direction is right]
*/
network_map
build_network(std::vector<std::string> network_dfn) {
    network_map network;

    std::vector<std::string> splt, elements;
    std::string nodeid, elementstr;
    std::string rmchars = "() ";
    size_t nrm = rmchars.size();
    for (const auto& line : network_dfn) {
        splt = stringsplit(line, " = ");
        nodeid = splt.front();
        elementstr = splt.back();
        for (size_t i=0; i < nrm; i++) {
            elementstr.erase(
                std::remove(elementstr.begin(), elementstr.end(), rmchars[i]),
                elementstr.end()
            );
        }
        network[nodeid] = stringsplit(elementstr, ",");
    }
    return network;
}


/**
 * Count the number of steps it takes to get from the A node the Z node,
 * given the network and the directions (sequence of lefts/rights).
 * Specify startnode.
 * Use 'checklast' if only the last char of the 3-char node ID needs to be a Z.
 * Otherwise, the Z node is 'ZZZ'.
*/
int
count_steps_az(network_map network,
               std::string directions,
               std::string startnode,
               bool checklast) {
    std::string nodeid = startnode;
    int steps = 0, ix;
    size_t dir_ix = 0;
    while (true) {
        steps++;
        ix = (directions[dir_ix] == 'L' ? 0 : 1);
        nodeid = network[nodeid][ix];
        if ((checklast && nodeid[2] == 'Z')
            || (nodeid.compare("ZZZ") == 0)) {
                break;
        }
        dir_ix++;
        if (dir_ix == directions.size()) {
            dir_ix = 0;
        }
    }
    return steps;
}


/**
 * Calculate least common multiple
 * https://stackoverflow.com/questions/4229870/c-algorithm-to-calculate-least-common-multiple-for-multiple-numbers
*/
long long
gcd(long long a, long long b) {
   return b == 0 ? a : gcd(b, a % b);

long long
lcm(long long a, long long b) {
    long long d = gcd(a, b);
    return d > 0 ? (a / d * b) : 0; 
}


int
main(int argc, char* argv[]) {
    // INPUT
            if (argc < 2) {
                std::cerr << "Provide filepath\n";
                return 1;
            }
            std::ifstream infile(argv[1]);
            if (!infile) {
                std::cerr << argv[1] << ": file not found\n";
                return 1;
            }
    ////////////////////////////////////////////////////////////////////////
    //
    // PARSE
    //
    std::vector<std::string> NETWORK_LINES;
    std::string DIRECTIONS;

    std::string line;
    int i = 0;
    while (std::getline(infile, line)) {
        if (i == 0) {
            DIRECTIONS = line;
            i++;
            continue;
        } else if (i == 1) {
            i++;
            continue;
        } else {
            NETWORK_LINES.push_back(line);
        }
    }

    network_map NETWORK = build_network(NETWORK_LINES);
    //
    // PART 1
    //
    int p1 = count_steps_az(NETWORK,   // network map
                            DIRECTIONS, // right/left directions
                            "AAA",     // startnode
                            false);    // comparelast: just need '..Z' and not 'ZZZ' to end.
    
    std::cout << "part 1 answer:\n" << p1 << std::endl;
    //
    // PART 2
    //
    std::vector<int> stepcounts;
    for (const auto& it : NETWORK) {
        if (it.first[2] == 'A') { // do for all nodes ending with A
            stepcounts.push_back(
                count_steps_az(NETWORK, DIRECTIONS, it.first, true)
            );
        }
    }
    // the number of steps needed before all A->Z paths terminate is the
    // least common multiple of the individual stepcounts
    long long p2 = std::accumulate(stepcounts.begin(), stepcounts.end(), 1LL, lcm);

    std::cout << "part 2 answer:\n" << p2 << std::endl;

    return 0;
}