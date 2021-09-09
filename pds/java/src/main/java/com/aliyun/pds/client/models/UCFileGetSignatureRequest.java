// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * UCFileGetSignatureRequest get file upload signature
 */
public class UCFileGetSignatureRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // action
    @NameInMap("action")
    public String action;

    // bucket
    @NameInMap("bucket")
    public String bucket;

    // content_md5
    @NameInMap("content_md5")
    public String contentMd5;

    // content_type
    @NameInMap("content_type")
    public String contentType;

    // date
    @NameInMap("date")
    public String date;

    // drive_id
    @NameInMap("drive_id")
    public String driveId;

    // headers
    @NameInMap("headers")
    public java.util.Map<String, ?> headers;

    // object_key
    @NameInMap("object_key")
    public String objectKey;

    // parameters
    @NameInMap("parameters")
    public java.util.Map<String, ?> parameters;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    public static UCFileGetSignatureRequest build(java.util.Map<String, ?> map) throws Exception {
        UCFileGetSignatureRequest self = new UCFileGetSignatureRequest();
        return TeaModel.build(map, self);
    }

    public UCFileGetSignatureRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UCFileGetSignatureRequest setAction(String action) {
        this.action = action;
        return this;
    }
    public String getAction() {
        return this.action;
    }

    public UCFileGetSignatureRequest setBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }
    public String getBucket() {
        return this.bucket;
    }

    public UCFileGetSignatureRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public UCFileGetSignatureRequest setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public UCFileGetSignatureRequest setDate(String date) {
        this.date = date;
        return this;
    }
    public String getDate() {
        return this.date;
    }

    public UCFileGetSignatureRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UCFileGetSignatureRequest setHeaders(java.util.Map<String, ?> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, ?> getHeaders() {
        return this.headers;
    }

    public UCFileGetSignatureRequest setObjectKey(String objectKey) {
        this.objectKey = objectKey;
        return this;
    }
    public String getObjectKey() {
        return this.objectKey;
    }

    public UCFileGetSignatureRequest setParameters(java.util.Map<String, ?> parameters) {
        this.parameters = parameters;
        return this;
    }
    public java.util.Map<String, ?> getParameters() {
        return this.parameters;
    }

    public UCFileGetSignatureRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
