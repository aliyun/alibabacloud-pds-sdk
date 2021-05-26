// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class IMMProject extends TeaModel {
    @NameInMap("canary_percent")
    public Long canaryPercent;

    @NameInMap("canary_project_name")
    public String canaryProjectName;

    @NameInMap("notify_endpoint")
    public String notifyEndpoint;

    @NameInMap("notify_topic_name")
    public String notifyTopicName;

    @NameInMap("project_name")
    public String projectName;

    @NameInMap("region")
    public String region;

    // 访问Project的角色ARN
    @NameInMap("role_arn")
    public String roleArn;

    public static IMMProject build(java.util.Map<String, ?> map) throws Exception {
        IMMProject self = new IMMProject();
        return TeaModel.build(map, self);
    }

    public IMMProject setCanaryPercent(Long canaryPercent) {
        this.canaryPercent = canaryPercent;
        return this;
    }
    public Long getCanaryPercent() {
        return this.canaryPercent;
    }

    public IMMProject setCanaryProjectName(String canaryProjectName) {
        this.canaryProjectName = canaryProjectName;
        return this;
    }
    public String getCanaryProjectName() {
        return this.canaryProjectName;
    }

    public IMMProject setNotifyEndpoint(String notifyEndpoint) {
        this.notifyEndpoint = notifyEndpoint;
        return this;
    }
    public String getNotifyEndpoint() {
        return this.notifyEndpoint;
    }

    public IMMProject setNotifyTopicName(String notifyTopicName) {
        this.notifyTopicName = notifyTopicName;
        return this;
    }
    public String getNotifyTopicName() {
        return this.notifyTopicName;
    }

    public IMMProject setProjectName(String projectName) {
        this.projectName = projectName;
        return this;
    }
    public String getProjectName() {
        return this.projectName;
    }

    public IMMProject setRegion(String region) {
        this.region = region;
        return this;
    }
    public String getRegion() {
        return this.region;
    }

    public IMMProject setRoleArn(String roleArn) {
        this.roleArn = roleArn;
        return this;
    }
    public String getRoleArn() {
        return this.roleArn;
    }

}
