import React from "react";
import { Bar } from "react-chartjs-2";
import "./Graphs.scss";
import { Chart as ChartJS } from "chart.js/auto";
import { Chart } from "react-chartjs-2";

export default function Graph(props) {
  var openIssue = props.openIssue;
  var closedIssue = props.closedIssue;
  var totalIssue = props.totalIssue;
  var openComment = props.openComment;
  var closedComment = props.closedComment;
  var totalComment = props.totalComment;
  var totalLabel = props.totalLabel;
  console.log("sth")
  console.log(openIssue)
  if (props.status === "issue") {
    return (
      <div className="GraphContainer">
        <Bar
          data={{
            labels: ["Open Issue Number", "Closed Issue Number"],
            datasets: [
              {
                label: "Issue Number",
                backgroundColor: "#D56543",
                borderColor: "rgba(0,0,0,1)",
                borderWidth: 2,
                data: [openIssue, closedIssue],
              },
            ],
          }}
          options={{
            title: {
              display: true,
              text: "Average Rainfall per month",
              fontSize: 20,
            },
            legend: {
              display: true,
              position: "right",
            },
          }}
        />
        <div className="total">Total Issue Number: {totalIssue}</div>
      </div>
    );
  } else if (props.status === "comment") {
    return (
      <div className="GraphContainer">
        <Bar
          data={{
            labels: ["Open Comment Number", "Closed Comment Number"],
            datasets: [
              {
                label: "Comment Number",
                backgroundColor: "#D56543",
                borderColor: "rgba(0,0,0,1)",
                borderWidth: 2,
                data: [openComment, closedComment],
              },
            ],
          }}
          options={{
            title: {
              display: true,
              text: "Average Rainfall per month",
              fontSize: 20,
            },
            legend: {
              display: true,
              position: "right",
            },
          }}
        />
        <div className="total">Total Comment Number: {totalComment}</div>
      </div>
      
    );
  }
  else  {
    return (
      <div className="GraphContainer">
        <Bar
          data={{
            labels: ["Closed Comment Number"],
            datasets: [
              {
                label: "Label Number",
                backgroundColor: "#D56543",
                borderColor: "rgba(0,0,0,1)",
                borderWidth: 2,
                data: [totalLabel],
              },
            ],
          }}
          options={{
            title: {
              display: true,
              text: "Average Rainfall per month",
              fontSize: 20,
            },
            legend: {
              display: true,
              position: "right",
            },
          }}
        />
      </div>
    );
  }
}
