package com.Rpg.service;

import com.Rpg.entity.Project;
import com.Rpg.entity.User;

public class UserServiceImplement implements UserService {


    @Override
    public Project createProject(String name, String desc, User user) {
        Project project = new Project();
        project.setName(name);
        project.setDescription(desc);
        project.setUser(user);

        //save to DB
        return project;
    }
}
