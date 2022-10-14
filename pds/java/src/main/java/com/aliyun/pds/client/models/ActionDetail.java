// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ActionDetail extends TeaModel {
    @NameInMap("create")
    public CreateDetail create;

    @NameInMap("delete")
    public DeleteDetail delete;

    @NameInMap("edit")
    public EditDetail edit;

    @NameInMap("move")
    public MoveDetail move;

    @NameInMap("rename")
    public RenameDetail rename;

    @NameInMap("restore")
    public RestoreDetail restore;

    @NameInMap("trash")
    public TrashDetail trash;

    public static ActionDetail build(java.util.Map<String, ?> map) throws Exception {
        ActionDetail self = new ActionDetail();
        return TeaModel.build(map, self);
    }

    public ActionDetail setCreate(CreateDetail create) {
        this.create = create;
        return this;
    }
    public CreateDetail getCreate() {
        return this.create;
    }

    public ActionDetail setDelete(DeleteDetail delete) {
        this.delete = delete;
        return this;
    }
    public DeleteDetail getDelete() {
        return this.delete;
    }

    public ActionDetail setEdit(EditDetail edit) {
        this.edit = edit;
        return this;
    }
    public EditDetail getEdit() {
        return this.edit;
    }

    public ActionDetail setMove(MoveDetail move) {
        this.move = move;
        return this;
    }
    public MoveDetail getMove() {
        return this.move;
    }

    public ActionDetail setRename(RenameDetail rename) {
        this.rename = rename;
        return this;
    }
    public RenameDetail getRename() {
        return this.rename;
    }

    public ActionDetail setRestore(RestoreDetail restore) {
        this.restore = restore;
        return this;
    }
    public RestoreDetail getRestore() {
        return this.restore;
    }

    public ActionDetail setTrash(TrashDetail trash) {
        this.trash = trash;
        return this;
    }
    public TrashDetail getTrash() {
        return this.trash;
    }

}
