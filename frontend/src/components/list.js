
import React, { Component } from 'react'
import axios from 'axios'

function RenderTeam({ team_list }) {
    let tl = team_list.map((individualMembers) => {
        console.log(JSON.stringify(individualMembers));
        return (
            <div>
                <img src={"http://localhost:8000/"+individualMembers.image} alt="Trial_Image" />
                <h1>{individualMembers.name}</h1>
                {/* <h1>{individualBlogs.id}</h1> */}
                <h2>{individualMembers.team}</h2>
                <p>{individualMembers.content}</p>
            </div>
        )
    })

    return(tl);
}

export default class Team extends Component {
    constructor(props) {
        super(props);

        this.state = {
            team_list: [],
        }
    }

    componentDidMount() {
        axios.get('http://localhost:8000/team/team_list/')
            .then((response) => {
                this.setState({
                    team_list: response.data,
                });
            })
            .catch((err) => {
                alert("Something went wrong!");
            })
    }

    render() {
        let renderTeam;
        if (this.state.team_list.length !== 0) {
            // eslint-disable-next-line array-callback-return

            renderTeam = <RenderTeam team_list={this.state.team_list} />
        }
        return (
            <div>
                {renderTeam}
            </div>
        )
    }
}