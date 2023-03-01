// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseAuditLogResponse extends TeaModel {
    /**
     * <p>客户端设备</p>
     */
    @NameInMap("ClientDevice")
    public String ClientDevice;

    /**
     * <p>客户端IP</p>
     */
    @NameInMap("ClientIP")
    public String ClientIP;

    /**
     * <p>客户端类型</p>
     */
    @NameInMap("ClientType")
    public String ClientType;

    /**
     * <p>客户端版本</p>
     */
    @NameInMap("ClientVersion")
    public String ClientVersion;

    /**
     * <p>操作时间</p>
     */
    @NameInMap("acted_at")
    public String actedAt;

    /**
     * <p>操作分类</p>
     */
    @NameInMap("action_category")
    public String actionCategory;

    /**
     * <p>操作类型</p>
     */
    @NameInMap("action_type")
    public String actionType;

    /**
     * <p>操作者ID</p>
     */
    @NameInMap("actor_id")
    public String actorId;

    /**
     * <p>操作者名称</p>
     */
    @NameInMap("actor_name")
    public String actorName;

    /**
     * <p>操作者类型</p>
     */
    @NameInMap("actor_type")
    public String actorType;

    @NameInMap("detail")
    public LogDetail detail;

    /**
     * <p>文件空间类型</p>
     */
    @NameInMap("file_path_type")
    public String filePathType;

    /**
     * <p>唯一标识一条日志</p>
     */
    @NameInMap("log_id")
    public String logId;

    /**
     * <p>对象ID</p>
     */
    @NameInMap("object_id")
    public String objectId;

    /**
     * <p>对象名</p>
     */
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
