#include "solver.hpp"
#include <iostream>
#include <sys/time.h>
#include "rlagent.hpp"

using namespace GameSolver::Connect4;

/*
 * Get micro-second precision timestamp
 * uses unix gettimeofday function
 */
unsigned long long getTimeMicrosec() {
  timeval NOW;
  gettimeofday(&NOW, NULL);
  return NOW.tv_sec*1000000LL + NOW.tv_usec;
}

/*
 * Main function.
 * Reads Connect 4 positions, line by line, from standard input
 * and writes one line per position to standard output containing:
 *  - score of the position
 *  - number of nodes explored
 *  - time spent in microsecond to solve the position.
 *
 *  Any invalid position (invalid sequence of move, or already won game)
 *  will generate an error message to standard error and an empty line to standard output.
 */
int main(int argc, char** argv) {

  Solver solver;
  RLAgent rl;

  bool weak = false;
  if(argc > 1 && argv[1][0] == '-' && argv[1][1] == 'w') weak = true;

  std::string line="44444";//ideal first moves

  for(int l = 1; l<10; l++) {
    Position P;
    if(P.play(line) != line.size())
    {
      std::cerr << "Line " << l << ": Invalid move " << (P.nbMoves()+1) << " \"" << line << "\"" << std::endl;
    }
    else
    {
      solver.reset();
      unsigned long long start_time = getTimeMicrosec();
      int score = solver.solve(P, weak);
      rl.setReward(score);
      unsigned long long end_time = getTimeMicrosec();
      std::cout << line << " " << score << " " << solver.getNodeCount() << " " << (end_time - start_time);
    }
    std::cout << std::endl;
  }
}
