import Graph from "./components/graph/Graph";
import "./app.scss";
import axios from "axios";
import React, { useEffect, useState } from "react";

const baseURL = "http://localhost:5000/";

function App() {
  const [OpenIssue, setOpenIssue] = useState(null);
  const [ClosedIssue, setClosedIssue] = useState(null);
  const [TotalIssue, setTotalIssue] = useState(null);
  const [OpenComment, setOpenComment] = useState(null);
  const [ClosedComment, setClosedComment] = useState(null);
  const [TotalComment, setTotalComment] = useState(null);
  const [TotalLabel, setTotalLabel] = useState(null);
  const [status, setStatus] = useState("");
  const [repo, setRepo] = useState(null);

  console.log(OpenComment)
  const setStatusText = (text) =>{
    setStatus(text);
  }
  const getFromApi = async () => {
    try {
      const data = await axios.get(baseURL).then((res) => {
        setOpenIssue(res.data.Open_issue_number);
        setClosedIssue(res.data.Closed_issue_number);
        setTotalIssue(res.data.Total_issue_number);

        setOpenComment(res.data.Open_comment_number);
        setClosedComment(res.data.Closed_comment_number);
        setTotalComment(res.data.Total_comment_number);
        setTotalLabel(res.data.Total_label_number);
        setRepo(res.data.Repository_name);
      });
    } catch (e) {
      console.log(e);
    }
  };
  useEffect(() => {
    getFromApi();
  }, []);

  return (
    <div className="app">
      <div className="header">
        <div className="buttonContainer">
          <div className="button" onClick={() => setStatusText("issue")} >Open-Closed Issue Numbers</div>
          <div className="button" onClick={() => setStatusText("comment")} >Open-Closed Comment Numbers</div>
          <div className="button" onClick={() => setStatusText("label")} >Label Number</div>
        </div>
      </div>

      <div className="graphs">
        <Graph
          status={status}
          RepoName={repo}
          openIssue={OpenIssue}
          closedIssue={ClosedIssue}
          totalIssue={TotalIssue}
          openComment={OpenComment}
          closedComment={ClosedComment}
          totalComment={TotalComment}
          totalLabel={TotalLabel}
        />
      </div>
    </div>
  );
}

export default App;
