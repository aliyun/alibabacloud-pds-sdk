<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ActionDetail extends Model
{
    /**
     * @var CreateDetail
     */
    public $create;

    /**
     * @var DeleteDetail
     */
    public $delete;

    /**
     * @var EditDetail
     */
    public $edit;

    /**
     * @var MoveDetail
     */
    public $move;

    /**
     * @var RenameDetail
     */
    public $rename;

    /**
     * @var RestoreDetail
     */
    public $restore;

    /**
     * @var TrashDetail
     */
    public $trash;
    protected $_name = [
        'create'  => 'create',
        'delete'  => 'delete',
        'edit'    => 'edit',
        'move'    => 'move',
        'rename'  => 'rename',
        'restore' => 'restore',
        'trash'   => 'trash',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->create) {
            $res['create'] = null !== $this->create ? $this->create->toMap() : null;
        }
        if (null !== $this->delete) {
            $res['delete'] = null !== $this->delete ? $this->delete->toMap() : null;
        }
        if (null !== $this->edit) {
            $res['edit'] = null !== $this->edit ? $this->edit->toMap() : null;
        }
        if (null !== $this->move) {
            $res['move'] = null !== $this->move ? $this->move->toMap() : null;
        }
        if (null !== $this->rename) {
            $res['rename'] = null !== $this->rename ? $this->rename->toMap() : null;
        }
        if (null !== $this->restore) {
            $res['restore'] = null !== $this->restore ? $this->restore->toMap() : null;
        }
        if (null !== $this->trash) {
            $res['trash'] = null !== $this->trash ? $this->trash->toMap() : null;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ActionDetail
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['create'])) {
            $model->create = CreateDetail::fromMap($map['create']);
        }
        if (isset($map['delete'])) {
            $model->delete = DeleteDetail::fromMap($map['delete']);
        }
        if (isset($map['edit'])) {
            $model->edit = EditDetail::fromMap($map['edit']);
        }
        if (isset($map['move'])) {
            $model->move = MoveDetail::fromMap($map['move']);
        }
        if (isset($map['rename'])) {
            $model->rename = RenameDetail::fromMap($map['rename']);
        }
        if (isset($map['restore'])) {
            $model->restore = RestoreDetail::fromMap($map['restore']);
        }
        if (isset($map['trash'])) {
            $model->trash = TrashDetail::fromMap($map['trash']);
        }

        return $model;
    }
}
