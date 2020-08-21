// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * the file op info
 */
public class FileDeltaResponse extends TeaModel {
    @NameInMap("current_category")
    public String currentCategory;

    @NameInMap("file")
    public BaseFileResponse file;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("op")
    public String op;

    public static FileDeltaResponse build(java.util.Map<String, ?> map) throws Exception {
        FileDeltaResponse self = new FileDeltaResponse();
        return TeaModel.build(map, self);
    }

    public FileDeltaResponse setCurrentCategory(String currentCategory) {
        this.currentCategory = currentCategory;
        return this;
    }
    public String getCurrentCategory() {
        return this.currentCategory;
    }

    public FileDeltaResponse setFile(BaseFileResponse file) {
        this.file = file;
        return this;
    }
    public BaseFileResponse getFile() {
        return this.file;
    }

    public FileDeltaResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public FileDeltaResponse setOp(String op) {
        this.op = op;
        return this;
    }
    public String getOp() {
        return this.op;
    }

}
