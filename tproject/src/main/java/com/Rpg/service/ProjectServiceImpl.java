package com.Rpg.service;

import com.Rpg.entity.Account;
import com.Rpg.entity.Project;
import com.Rpg.entity.Status;
import com.Rpg.repository.AccountRepository;
import com.Rpg.repository.ProjectRepo;
import com.google.gson.Gson;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.List;

public class ProjectServiceImpl implements ProjectService {

    private AccountRepository accountRepository;
    private ProjectRepo projectRepo;

    @Autowired
    public ProjectServiceImpl(AccountRepository accountRepository, ProjectRepo projectRepo) {
        this.accountRepository = accountRepository;
        this.projectRepo = projectRepo;
    }

    @Override
    public void addAccounts(Long projectId) {
        Project project = projectRepo.getById(projectId);
        List<Account> list = accountRepository.getAccountByStatus(Status.NEW);
        project.setAccounts(list);
        projectRepo.save(project);
    }
}
