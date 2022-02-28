// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseAuditLogResponse extends TeaModel {
    // 客户端设备
    @NameInMap("ClientDevice")
    public String ClientDevice;

    // 客户端IP
    @NameInMap("ClientIP")
    public String ClientIP;

    // 客户端类型
    @NameInMap("ClientType")
    public String ClientType;

    // 客户端版本
    @NameInMap("ClientVersion")
    public String ClientVersion;

    // 操作时间
    @NameInMap("acted_at")
    public String actedAt;

    // 操作分类
    @NameInMap("action_category")
    public String actionCategory;

    // 操作类型
    @NameInMap("action_type")
    public String actionType;

    // 操作者ID
    @NameInMap("actor_id")
    public String actorId;

    // 操作者名称
    @NameInMap("actor_name")
    public String actorName;

    // 操作者类型
    @NameInMap("actor_type")
    public String actorType;

    @NameInMap("detail")
    public LogDetail detail;

    // 文件空间类型
    @NameInMap("file_path_type")
    public String filePathType;

    // 唯一标识一条日志
    @NameInMap("log_id")
    public String logId;

    // 对象ID
    @NameInMap("object_id")
    public String objectId;

    // 对象名
    @NameInMap("object_name")
    public String objectName;

    public static BaseAuditLogResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseAuditLogResponse self = new BaseAuditLogResponse();
        return TeaModel.build(map, self);
    }

    public BaseAuditLogResponse setClientDevice(String ClientDevice) {
        this.ClientDevice = ClientDevice;
        return this;
    }
    public String getClientDevice() {
        return this.ClientDevice;
    }

    public BaseAuditLogResponse setClientIP(String ClientIP) {
        this.ClientIP = ClientIP;
        return this;
    }
    public String getClientIP() {
        return this.ClientIP;
    }

    public BaseAuditLogResponse setClientType(String ClientType) {
        this.ClientType = ClientType;
        return this;
    }
    public String getClientType() {
        return this.ClientType;
    }

    public BaseAuditLogResponse setClientVersion(String ClientVersion) {
        this.ClientVersion = ClientVersion;
        return this;
    }
    public String getClientVersion() {
        return this.ClientVersion;
    }

    public BaseAuditLogResponse setActedAt(String actedAt) {
        this.actedAt = actedAt;
        return this;
    }
    public String getActedAt() {
        return this.actedAt;
    }

    public BaseAuditLogResponse setActionCategory(String actionCategory) {
        this.actionCategory = actionCategory;
        return this;
    }
    public String getActionCategory() {
        return this.actionCategory;
    }

    public BaseAuditLogResponse setActionType(String actionType) {
        this.actionType = actionType;
        return this;
    }
    public String getActionType() {
        return this.actionType;
    }

    public BaseAuditLogResponse setActorId(String actorId) {
        this.actorId = actorId;
        return this;
    }
    public String getActorId() {
        return this.actorId;
    }

    public BaseAuditLogResponse setActorName(String actorName) {
        this.actorName = actorName;
        return this;
    }
    public String getActorName() {
        return this.actorName;
    }

    public BaseAuditLogResponse setActorType(String actorType) {
        this.actorType = actorType;
        return this;
    }
    public String getActorType() {
        return this.actorType;
    }

    public BaseAuditLogResponse setDetail(LogDetail detail) {
        this.detail = detail;
        return this;
    }
    public LogDetail getDetail() {
        return this.detail;
    }

    public BaseAuditLogResponse setFilePathType(String filePathType) {
        this.filePathType = filePathType;
        return this;
    }
    public String getFilePathType() {
        return this.filePathType;
    }

    public BaseAuditLogResponse setLogId(String logId) {
        this.logId = logId;
        return this;
    }
    public String getLogId() {
        return this.logId;
    }

    public BaseAuditLogResponse setObjectId(String objectId) {
        this.objectId = objectId;
        return this;
    }
    public String getObjectId() {
        return this.objectId;
    }

    public BaseAuditLogResponse setObjectName(String objectName) {
        this.objectName = objectName;
        return this;
    }
    public String getObjectName() {
        return this.objectName;
    }

}
