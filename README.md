# Final Project: LIS590DV - Fall 2017

Your final project is composed of four parts.  You will work in groups of three
or four people; each person will be expected to participate in the project.

Note that in some cases, the descriptions of *what* you are to visualize are
somewhat vague.  This is in keeping with our discussion of carefully choosing
the story you want to tell.  You're going to be called upon in this assignment
to examine the data, and then within the rough outlines of the discussion,
construct a visualization that "answers" the posed question.

There are a few important notes:

 * All of the source code must be provided.
 * Use GitHub to version your code and your writeup.  This will also be used to
   verify individual contributions.
 * The writeup will be evaluated.
 * A "visualization" does not mean a single plot; it is broadly defined to
   include linked visualizations, collections of plots, etc.

## Component 1: Transportable Array Interactive

**Concept**: Show the how the transportable array responded to an earthquake.

![](part1/example.png)

Your first dataset will be based on data from the transportable array, for the
four hours following the Tohoku earthquake.  This data is available in two
files on the LIS590 server, under the directory
`/srv/nbgrader/data/transportable_array`.

 * `location.txt` is a tsv containing the latitude and longitude.  The final
   two columns are irrelevant data and can be discarded.
 * `data_tohoku_norm_transpose.csv` is a csv containing each of the 438
   stations in a column, and each row is subsequent seconds from the
   earthquake.

You will make one interactive visualization.  This should have a map, a time
slider, a spectrogram, and a line plot of the currently selected detector.

A spectrogram is a visualization in which a 2D array is created, showing the
normalized values from a collection of 1D arrays.  In principle, the input from
the `data_tohoku_norm_transpose.csv` file can be very easily converted into
this.  However, this will give an odd stratification of the array detectors,
because they're just ordered however they are in the file.  Instead, you should
create a *new* ordering of the array detectors.  Compute (you can use the
`haversine` package) the distance from the Tohoku quake itself, and use this to
order the detectors from closest to furthest.  Order them this way in the
spectrogram.

Display the locations of each detector in the transportable array on a map of
the United States; the color of each mark should represent the value of the
wave at the currently selected time.

The waveform of each selected detector (selected by hovering, selecting from a
dropdown, or by clicking on a detector) should be displayed as a line plot.

Annotate the spectrogram to indicate current time and selected detector.

 * Extra: Turn each into audio.  (Don't autoplay though.)


## Component 2: Transportable Array Movie

Make a time-varying visualization of the transportable array and how it
responds to an earthquake.  You will be graded on the information that is
communicated and the aesthetics.

This does not have to be a strictly quantitative visualization, and it can be
done in any software.  You may choose to augment this with 

Your writeup of this should *very* clearly state what you intend for
individuals to get out of the visualization as well as how you did it.  Because
this is an open-ended problem, by design, you *must* describe what you intended
to communicate.

This should be uploaded to mediaspace.illinois.edu and any source code placed
in this repository.

## Component 3: UFO database and supplemental data

For this component, you are to build an interactive visualization of the UFO
sighting database we have been working with.

As a reminder, you can load this data with:

```
#!python
names = ["date", "city", "state", "country", "shape", "duration_seconds",
         "duration_reported", "description", "report_date", "latitude",
         "longitude"]

fn = "/srv/nbgrader/data/ufo-scrubbed-geocoded-time-standardized.csv",
ufo = pd.read_csv(fn, names = names, parse_dates = ["date", "report_date"])
```

Your visualization should be interactive; you may find it easiest to
use [bqplot](http://bqplot.readthedocs.org/) to build this visualization.  It
should display the following pieces of information:

 * A map of the United States, where the states are colored either by the total
   sightings in each state over the selected time period, or the total time in
   sightings.
 * A plot displaying the total number of sightings in whichever state is
   highlighted, aggregated so that it is a function of the *year*.
 * A plot displaying the total duration of sightings in whichever state is
   highlighted, aggregated so that it is a function of the *year*.
 * Tooltips should appear when hovering over the state with useful information
   about the state (either from the UFO database or elsewhere.)

Your interactive visualization must have the following modifiable parts:

 * Which field is being displayed: total sightings or total time.
 * Time period being visualized: there should be some widget or display
   mechanism that can be subselected; one possibility would be to show the
   total number of sightings over the entire database (aggregated by year) and
   allow the user to click and drag to highlight specific times regions.  When
   it is subselected, this should change the display in the map component.

The final component of this visualization will be to normalize based on some
other piece of information about the state.  For instance, this could be taking
the number of sightings and dividing it by the (modern-day, or per-year) population
of each state.  There are *many* different fields that these could be
normalized based on; allowing for interactivity in choosing which normalizing
field would be useful.

Data about the states can be found at many different places online, and items
from QuickFacts can be found at:

https://data.world/aaronhoffman/census-gov-state-quickfacts

Note that this may require using an abbreviation terminology known as FIPS, for
Federal Information Processing Standards.  In `part3/starter_code.py` you can
see how to obtain the FIPS number for each state, as well as one way of
plotting data in `bqplot` based on FIPS-keyed information.

## Component 4: Infographic 

Concept: From the visualization you constructed in either component 1 or
component 3, construct a narrative. You should take the visual output, possibly
modifying it (potentially with something like photoshop or gimp) to fit the
style of the rest of your text.

Your output should be in the form of an "infographic." This should include the
visualization, narrative text, and should be designed to convey a story of your
own choosing.

This component will be graded on style of presentation, aesthetics,
representation of the data, and breakdown of the information for understanding
by lay people.

## Final Writeup

You will be tasked with providing a writeup of your visualizations as well.
Each should be in markdown form and in the directory with your visualizations.
These should describe in some detail:

 * Why you took the approach you did
 * Strengths of your approach
 * Weaknesses of your approach
 * What you wished you had been able to do (if anything)
 * Who in the group contributed each part of the visualization (from code, data
   management, data cleaning, writeup, and so on.)
