import java.awt.*;
import java.awt.geom.*;
import java.util.*;
import java.io.*;
import javax.imageio.*;
import java.util.List;
import java.util.ArrayList;
import java.awt.image.BufferedImage;

import com.topcoder.marathon.*;

public class BioSlimeTester extends MarathonAnimatedVis {
  //parameter ranges
  private static final int minN = 10, maxN = 30; // grid size range
  private static final int minD = 1, maxD = 10; // number of depots
  private static final int minH = 1, maxH = 20; // number of harvesters
  private static final double minS = 0.01, maxS = 0.05;  // slime spawning probability range
  private static final double minP = 0.01, maxP = 0.05; // slime spreading probability range
  private static final double minW = 0.1, maxW = 0.2;  // wall spawning probability range

  //Inputs
  private int N;            //grid size
  private int D;            //number of depots
  private int H;            //number of harvesters
  private int C;            //capacity of a harverster
  private double slimeP;    //slime spawn probability  
  private double spreadP;   //spread probability  
  private double wallP;     //wall probability

  //Constants other
  private static final char Wall = 'W';
  private static final char Depot = 'd';
  private static final char Slime = 's';
  private static final char Harvester = 'H';
  private static final char Empty = '.';
  private static final int[] dr = {0,  -1,  0,  1};
  private static final int[] dc = {-1,  0,  1,  0};
  private static final int maxTurns=1000;

  //Graphics

  //State Control
  private char[][] grid; 
  private int numTurns;
  private int turn;
  private int numHarvesters;
  private int numDepots, numStartDepots;
  private int numSlime;    //number of alive slime
  private int bioGathered; //biofuel gathered and deposited
  private int bioUndelivered; //biofuel in hand and not delivered yet
  private int[] bioDepots; //biofuel collected and each depot
  private int[] carry;     //number of slime carried by harvester
  private int[] entityR;   //row of harvesters
  private int[] entityC;   //column of harvesters
  private int[] locDepots; //Depot locations encoded as r*N+c
  private boolean[][] visited; //used to see if all cells can be reached
  private boolean[] visGathered; //used for visualisation of the depot receiving fuel
  private int score;

  protected void generate()
  {
    N = randomInt(minN, maxN);
    D = randomInt(minD, maxD);
    C = randomInt(1, N);
    H = randomInt(minH, maxH);
    slimeP = randomDouble(minS, maxS);
    spreadP = randomDouble(minP, maxP);
    wallP = randomDouble(minW, maxW);

    //Special cases
    if (seed == 1)
    {
      N = minN;
      D = 2;
      C = 4;
      H = 4;
      slimeP = 0.02;
      spreadP = 0.03;
      wallP = minW;
    }
    else if (seed == 2)
    {
      N = maxN;
      D = maxD;
      C = N;
      H = maxH;
      slimeP = maxS;
      spreadP = maxP;
      wallP = maxW;
    }

    //User defined parameters
    if (parameters.isDefined("N")) 
    {
      N = randomInt(parameters.getIntRange("N"), minN, maxN);
      C = randomInt(1, N);
    }
    if (parameters.isDefined("D")) D = randomInt(parameters.getIntRange("D"), minD, maxD);
    if (parameters.isDefined("C")) C = randomInt(parameters.getIntRange("C"), 1, N);
    if (parameters.isDefined("H")) H = randomInt(parameters.getIntRange("H"), minH, maxH);
    if (parameters.isDefined("S")) slimeP = randomDouble(parameters.getDoubleRange("S"), minS, maxS);
    if (parameters.isDefined("P")) spreadP = randomDouble(parameters.getDoubleRange("P"), minP, maxP);
    if (parameters.isDefined("W")) wallP = randomDouble(parameters.getDoubleRange("W"), minW, maxW);

    bioDepots = new int[D];
    visGathered = new boolean[D];
    bioUndelivered = 0;
    bioGathered = 0;

    //initialize grid
    while (true)
    {
      grid = new char[N][N];
      carry = new int[H];
      entityC = new int[H];
      entityR = new int[H];
      locDepots = new int[D];
      numSlime = 0;
      numHarvesters = 0;
      numDepots = 0;
      int emptyCells = N*N;
    
      // place slime and walls
      for (int i=0; i<N; i++)
        for (int k=0; k<N; k++)
        {
          double p = randomDouble(0,1);
          if (p<slimeP)
          {
            grid[i][k] = Slime;
            numSlime++;
          }
          else if (p<slimeP+wallP)
          {
            grid[i][k] = Wall;
            emptyCells--;
          }
          else 
          {
            grid[i][k] = Empty;
          }            
        }

      // place depots
      for (int i=0;i<D;i++)
      {
        int r,c;
        do
        {
          r = randomInt(1, N-2);
          c = randomInt(1, N-2);
        } while (grid[r][c]!=Empty || grid[r+1][c]==Slime || grid[r-1][c]==Slime || 
                 grid[r-1][c-1]==Slime || grid[r][c-1]==Slime || grid[r+1][c-1]==Slime ||
                 grid[r-1][c+1]==Slime || grid[r][c+1]==Slime || grid[r+1][c+1]==Slime);
        grid[r][c] = Depot;
        locDepots[numDepots] = r*N+c;
        numDepots++;
        emptyCells--;
      }
      // Make sure everything is reachable by harvesters
      int reachable = 0;
      for (int i=0; i<N; i++)
        for (int k=0; k<N; k++)
          if (grid[i][k]==Empty && reachable==0)
          {
            visited = new boolean[N][N];
            reachable = countReachable(i,k);
          }
      // place harvesters
      for (int i=0;i<H;i++)
      {
        int r,c;
        do
        {
          r = randomInt(0, N-1);
          c = randomInt(0, N-1);
        } while (grid[r][c]!=Empty);
        grid[r][c] = Harvester;
        carry[numHarvesters] = 0;
        entityC[numHarvesters] = c;
        entityR[numHarvesters] = r;
        numHarvesters++;
      }

      if (reachable==emptyCells && numDepots>0 && numSlime>0 && numHarvesters>0)
        break;
    }

    numStartDepots = numDepots;
    if (debug)
    {
      System.out.println("Grid size, N = " + N);
      System.out.println("Depots, D = " + D);
      System.out.println("Harvesters, H = " + H);
      System.out.println("Carry Capacity, C = " + C);
      System.out.println("Slime Probability = " + slimeP);
      System.out.println("Wall Probability = " + wallP);
      System.out.println("Spread Probability = " + spreadP);
      System.out.println("Grid:");
      for (int row = 0; row < N; row++)
      {
        for (int col = 0; col < N; col++)
          System.out.print(grid[row][col]);
        System.out.println();
      }
    }
  }

  protected int countReachable(int r, int c)
  {
    Queue<int[]> queue = new LinkedList<>();
    queue.add(new int[]{r, c});
    visited[r][c] = true;
    int count = 1;

    while (!queue.isEmpty()) 
    {
      int[] cell = queue.poll();
      int row = cell[0], col = cell[1];

      for (int d = 0; d < 4; d++) 
      {
          int nr = row + dr[d];
          int nc = col + dc[d];

          if (nr >= 0 && nr < N && nc >= 0 && nc < N && 
              (grid[nr][nc] == Empty ||  grid[nr][nc] == Slime) && 
              !visited[nr][nc]) 
          {
            visited[nr][nc] = true;
            queue.add(new int[]{nr, nc});
            count++;
          }
      }
    }
    return count;
  }

  protected boolean isMaximize() {
      return true;
  }

  protected double run() throws Exception
  {
    init();
    return runAuto();
  }

  protected boolean inGrid(int r, int c)
  {
    return r>=0 && r<N && c>=0 && c<N;
  }

  protected boolean adjacentSlime(int r, int c)
  {
    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i], nc = c + dc[i];
        if (nr >= 0 && nr < N && nc >= 0 && nc < N && grid[nr][nc] == Slime) {
            return true;
        }
    }
    return false;
  }

  protected double runAuto() throws Exception
  {
    double score = callSolution();
    if (score < 0) {
      if (!isReadActive()) return getErrorScore();
      return fatalError();
    }
    return score;
  }

  protected void timeout() {
    addInfo("Time", getRunTime());
    update();
  }

  private double callSolution() throws Exception
  {
    writeLine(""+N);
    writeLine(""+C);
    writeLine(""+H);
    for (int i=0;i<H;i++)
      writeLine(""+entityR[i]+" "+entityC[i]);
    // print the grid
    for (int r = 0; r < N; r++)
      for (int c = 0; c < N; c++)
        writeLine(""+grid[r][c]);
    flush();    
    if (!isReadActive()) return -1;

    score = 0;

    updateState();

    List<int[]> newSlimeCells = new ArrayList<>();
    try
    {
      for (turn=1; turn<=maxTurns; turn++) 
      {
        //read solution output
        startTime();
        String line=readLine();
        stopTime();

        for (int k=0;k<D;k++) visGathered[k] = false; 

        // Move harvesters
        String[] temp = line.trim().split(" ");
        if (temp.length%2!=0)
        {
          return fatalError("Cannot parse your output. Should be a multiple of 2 in the format h M h M ...");
        } else
        {
          boolean[] moved = new boolean[H];
          for (int i=0; i<temp.length; i+=2)
          {
            try
            {
              int idx = Integer.parseInt(temp[i]);
              if (idx<0 || idx>=H) return fatalError("Harvester index out of bounds. Should be between 0 and "+(H-1)+", inclusive.");
              if (temp[i+1].length()!=1)
              {
                return fatalError("Invalid move, should be a single character U,D,L,R or X.");
              }
              if (moved[idx])
              {
                return fatalError("Harvester already moved, can't move a harvester multiple times in the same turn.");
              }
              moved[idx] = true;
              char dir = temp[i+1].charAt(0);
              int nrow = entityR[idx];
              int ncol = entityC[idx];
              int row = nrow;
              int col = ncol;
              if (dir=='U') nrow = row-1;
              else if (dir=='D') nrow = row+1;
              else if (dir=='L') ncol = col-1;
              else if (dir=='R') ncol = col+1;
              else if (dir=='X') continue; // Stand still
              else 
              {
                return fatalError("Invalid move, should be U,D,L,R or X.");
              }

              if (!inGrid(nrow, ncol))
              {
                return fatalError("Trying to move harvester outside of grid.");
              }
              if (grid[nrow][ncol]==Wall)
              {
                return fatalError("Invalid move, harvester moving into a wall.");
              }
              if (grid[nrow][ncol]==Slime)
              {
                if (carry[idx]>=C)
                {
                  return fatalError("Invalid move, harvester already at full capacity, can not move into slime.");
                }
                else
                {
                  carry[idx]++;
                  bioUndelivered++;
                  numSlime--;
                  grid[row][col] = Empty;
                  grid[nrow][ncol] = Harvester;
                  entityC[idx] = ncol;
                  entityR[idx] = nrow;
                }
              }
              else if (grid[nrow][ncol]==Depot)
              {
                // Increment the total fuel collected
                bioGathered += carry[idx];
                bioUndelivered -= carry[idx];
                // Keep track of the amount of fuel delivered to each depot
                for (int k=0;k<D;k++)
                  if (locDepots[k]==nrow*N+ncol && carry[idx]>0)
                  {
                    bioDepots[k] += carry[idx];
                    visGathered[k] = true;
                    break;
                  }
                // Reset harvester carry amount
                carry[idx] = 0;
              } else if (grid[nrow][ncol]==Harvester)
              {
                return fatalError("Invalid move, harvester moving into a harvester.");
              } else if (grid[nrow][ncol]==Empty)
              {
                grid[row][col] = Empty;
                grid[nrow][ncol] = Harvester;
                entityC[idx] = ncol;
                entityR[idx] = nrow;
              }
            }
            catch (Exception e)
            {
              if (debug) System.out.println(e.toString());
              return fatalError("Cannot parse your output");      
            }
          }
        }

        // Spawn slime
        newSlimeCells.clear();
        for (int r = 0; r < N; r++)
          for (int c = 0; c < N; c++)
          {
            double p = randomDouble(0,1); // always generate the random number in order to keep slime behaviour more consistent. 
            if ((grid[r][c]==Empty || grid[r][c]==Depot) && adjacentSlime(r,c))
            {
              if (p<spreadP)
              {
                newSlimeCells.add(new int[]{r, c});
                numSlime++;
                if (grid[r][c]==Depot) // Destroying a depot.
                {
                  numDepots--;
                }
              }
            }
          }
            
        // Update grid with new slime
        for (int[] cell : newSlimeCells) {
            grid[cell[0]][cell[1]] = Slime;
        }
        
        score = Math.max(0, N*N + bioGathered - numSlime);
        if (!parameters.isDefined("noanimate") || turn==maxTurns) updateState();

        // Write out time elapsed
        writeLine(""+getRunTime());
        // Write out harvester load
        for (int i=0;i<H;i++)
          writeLine(""+carry[i]);
        // Write out new grid
        for (int r = 0; r < N; r++)
          for (int c = 0; c < N; c++)
            writeLine(""+grid[r][c]);
        flush();    

      }
    }
    catch (Exception e) {
      if (debug) System.out.println(e.toString());
      updateState();
      return fatalError("Cannot parse your output");
    }
    
    return score;
  }

  protected void updateState()
  {
    if (hasVis())
    {
      synchronized (updateLock) {
        addInfo("Time",  getRunTime());
        addInfo("Turns", turn);
        addInfo("Active Slime", numSlime);
        addInfo("BioFuel Collected", bioGathered);
        addInfo("BioFuel Undelivered", bioUndelivered);        
        addInfo("Depots", ""+numDepots+" / "+numStartDepots); 
        addInfo("Score", shorten(score));
      }
      updateDelay();
    }
  }


  protected void paintContent(Graphics2D g)
  {
    g.setStroke(new BasicStroke(0.005f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));                          
    adjustFont(g, Font.SANS_SERIF, Font.BOLD, String.valueOf("1"), new Rectangle2D.Double(0, 0, 0.5, 0.5));

    //draw grid      
    for (int r = 0; r < N; r++)
      for (int c = 0; c < N; c++)
      {
        g.setColor(Color.white);
        g.fillRect(c, r, 1, 1);
        g.setColor(Color.gray);       
        g.drawRect(c, r, 1, 1);      
      }  
    //draw grid objects
    for (int r = 0; r < N; r++)
      for (int c = 0; c < N; c++)
      {            
        if (grid[r][c]!=Empty)
        {
          if (grid[r][c]==Harvester) continue;
          else if (grid[r][c]==Wall) g.setColor(Color.black);
          else if (grid[r][c]==Slime) g.setColor(Color.green);
          else if (grid[r][c]==Depot) g.setColor(Color.orange);
          g.fillRect(c, r, 1, 1);
        }
      }

    // draw depot stats
    g.setStroke(new BasicStroke(0.1f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND)); 
    for (int i=0;i<D;i++)
    {
      int c = locDepots[i]%N;
      int r = locDepots[i]/N;
      if (grid[r][c]==Depot) // Depot still active
      {
        if (visGathered[i]) // received fuel in this turn, highlight it
        {
          g.setColor(Color.blue);
          g.fillRect(c, r, 1, 1);
        }
        g.setColor(Color.red);
        drawString(g, ""+bioDepots[i], new Rectangle2D.Double(c+0.5, r+0.5, 0, 0)); 
      } else // Depot destroyed
      {
        g.setColor(Color.orange);  
        g.drawRect(c, r, 1, 1);  
        g.setColor(Color.black);
        drawString(g, ""+bioDepots[i], new Rectangle2D.Double(c+0.5, r+0.5, 0, 0)); 
      }
    }
    g.setStroke(new BasicStroke(0.005f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND)); 

    // draw harvesters
    for (int i=0;i<H;i++)
    {
      if (carry[i]==0)
        g.setColor(Color.cyan);
      else
      {
        int ci = 255*carry[i]/C;
        g.setColor(new Color(ci, 0, 255-ci));
      }
       // g.setColor(Color.blue);
      Ellipse2D t = new Ellipse2D.Double(entityC[i] + 0.05, entityR[i] + 0.05, 0.9, 0.9);
      g.fill(t);
      
      g.setColor(Color.white);
      drawString(g, ""+carry[i], new Rectangle2D.Double(entityC[i]+0.5, entityR[i]+0.5, 0, 0)); 
    }

  }

  private double shorten(double a)
  {
    return (double)Math.round(a * 1000.0) / 1000.0;
  }

  private void init()
  {
    if (hasVis())
    {
      setDefaultDelay(1000);    //this needs to be first
   
      setContentRect(0, 0, N, N);
      setInfoMaxDimension(5, 11);

      addInfo("Seed", seed);
      addInfo("N", N);
      addInfo("D", D);
      addInfo("C", C);
      addInfo("H", H);
      addInfo("Slime Prob", shorten(slimeP));
      addInfo("Spread Prob", shorten(spreadP));
      addInfo("Wall Prob", shorten(wallP));

      addInfoBreak();      
      addInfo("Time", "-");     
      addInfo("Turns", "-");
      addInfo("Active Slime", numSlime);
      addInfo("BioFuel Collected", bioGathered);
      addInfo("BioFuel Undelivered", bioUndelivered);  
      addInfo("Depots", "-");   
      addInfo("Score", "-");        
      update();
    }
  }

  public static void main(String[] args) {
      new MarathonController().run(args);
  }
}
