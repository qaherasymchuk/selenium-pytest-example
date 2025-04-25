@example
Feature: Screenshot of streamer page
  Scenario: User is able to find and open streamer page
    Given Twitch home page is opened
    When user accept cookies and advertising choices
    And open search page
    And search for "StarCraft II"
    And switch to videos
    And scroll down 2 times
    And select one streamer
    And close any popups before start video
    And wait until video is loaded
    And save screenshot and page source as test_streamer_video file
    Then test_streamer_video screenshot and page source files are present
