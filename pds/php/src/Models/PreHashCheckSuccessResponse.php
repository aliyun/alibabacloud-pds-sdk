<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Pre hash check Response.
 */
class PreHashCheckSuccessResponse extends Model
{
    /**
     * @description code
     *
     * @var string
     */
    public $code;

    /**
     * @description file_name
     *
     * @var string
     */
    public $fileName;

    /**
     * @description message
     *
     * @var string
     */
    public $message;

    /**
     * @description parent_file_id
     *
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     *
     * @var string
     */
    public $parentFileId;

    /**
     * @description pre_hash
     *
     * @var string
     */
    public $preHash;
    protected $_name = [
        'code'         => 'code',
        'fileName'     => 'file_name',
        'message'      => 'message',
        'parentFileId' => 'parent_file_id',
        'preHash'      => 'pre_hash',
    ];

    public function validate()
    {
        Model::validateRequired('parentFileId', $this->parentFileId, true);
        Model::validateMaxLength('parentFileId', $this->parentFileId, 50);
        Model::validateMinLength('parentFileId', $this->parentFileId, 40);
        Model::validatePattern('parentFileId', $this->parentFileId, '[a-z0-9]{1,50}');
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->code) {
            $res['code'] = $this->code;
        }
        if (null !== $this->fileName) {
            $res['file_name'] = $this->fileName;
        }
        if (null !== $this->message) {
            $res['message'] = $this->message;
        }
        if (null !== $this->parentFileId) {
            $res['parent_file_id'] = $this->parentFileId;
        }
        if (null !== $this->preHash) {
            $res['pre_hash'] = $this->preHash;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return PreHashCheckSuccessResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['code'])) {
            $model->code = $map['code'];
        }
        if (isset($map['file_name'])) {
            $model->fileName = $map['file_name'];
        }
        if (isset($map['message'])) {
            $model->message = $map['message'];
        }
        if (isset($map['parent_file_id'])) {
            $model->parentFileId = $map['parent_file_id'];
        }
        if (isset($map['pre_hash'])) {
            $model->preHash = $map['pre_hash'];
        }

        return $model;
    }
}
