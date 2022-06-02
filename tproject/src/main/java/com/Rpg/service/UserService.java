package com.Rpg.service;

import com.Rpg.entity.Project;
import com.Rpg.entity.User;

public interface UserService {

    Project createProject(String name, String desc, User user);


}
