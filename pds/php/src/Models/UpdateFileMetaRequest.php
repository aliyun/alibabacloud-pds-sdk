<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 更新文件元数据.
 */
class UpdateFileMetaRequest extends Model
{
    public $headers;

    /**
     * @description check_name_mode
     *
     * @var string
     */
    public $checkNameMode;

    /**
     * @var string
     */
    public $customIndexKey;

    /**
     * @description description
     * type: string
     * @example description
     *
     * @var string
     */
    public $description;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @var string
     */
    public $encryptMode;

    /**
     * @description file_id
     *
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     *
     * @var string
     */
    public $fileId;

    /**
     * @var string
     */
    public $fileIdPath;

    /**
     * @description hidden
     * type: boolean
     * @example false
     *
     * @var bool
     */
    public $hidden;

    /**
     * @description labels
     *
     * @example label1, label2
     *
     * @var string[]
     */
    public $labels;

    /**
     * @var string
     */
    public $meta;

    /**
     * @description name
     *
     * @example ccp.jpg
     *
     * @var string
     */
    public $name;

    /**
     * @var string
     */
    public $referer;

    /**
     * @var string
     */
    public $shareId;

    /**
     * @var string
     */
    public $signToken;

    /**
     * @description starred
     * type: boolean
     * @example false
     *
     * @var bool
     */
    public $starred;

    /**
     * @description user_meta
     *
     * @example user_meta
     *
     * @var string
     */
    public $userMeta;
    protected $_name = [
        'checkNameMode'  => 'check_name_mode',
        'customIndexKey' => 'custom_index_key',
        'description'    => 'description',
        'driveId'        => 'drive_id',
        'encryptMode'    => 'encrypt_mode',
        'fileId'         => 'file_id',
        'fileIdPath'     => 'file_id_path',
        'hidden'         => 'hidden',
        'labels'         => 'labels',
        'meta'           => 'meta',
        'name'           => 'name',
        'referer'        => 'referer',
        'shareId'        => 'share_id',
        'signToken'      => 'sign_token',
        'starred'        => 'starred',
        'userMeta'       => 'user_meta',
    ];
    protected $_default = [
        'checkNameMode' => 'ignore',
        'hidden'        => 'false',
        'starred'       => 'false',
    ];

    public function validate()
    {
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMaxLength('name', $this->name, 1024);
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMinLength('name', $this->name, 1);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->checkNameMode) {
            $res['check_name_mode'] = $this->checkNameMode;
        }
        if (null !== $this->customIndexKey) {
            $res['custom_index_key'] = $this->customIndexKey;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->encryptMode) {
            $res['encrypt_mode'] = $this->encryptMode;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->fileIdPath) {
            $res['file_id_path'] = $this->fileIdPath;
        }
        if (null !== $this->hidden) {
            $res['hidden'] = $this->hidden;
        }
        if (null !== $this->labels) {
            $res['labels'] = $this->labels;
        }
        if (null !== $this->meta) {
            $res['meta'] = $this->meta;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->referer) {
            $res['referer'] = $this->referer;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->signToken) {
            $res['sign_token'] = $this->signToken;
        }
        if (null !== $this->starred) {
            $res['starred'] = $this->starred;
        }
        if (null !== $this->userMeta) {
            $res['user_meta'] = $this->userMeta;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return UpdateFileMetaRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['check_name_mode'])) {
            $model->checkNameMode = $map['check_name_mode'];
        }
        if (isset($map['custom_index_key'])) {
            $model->customIndexKey = $map['custom_index_key'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['encrypt_mode'])) {
            $model->encryptMode = $map['encrypt_mode'];
        }
        if (isset($map['file_id'])) {
            $model->fileId = $map['file_id'];
        }
        if (isset($map['file_id_path'])) {
            $model->fileIdPath = $map['file_id_path'];
        }
        if (isset($map['hidden'])) {
            $model->hidden = $map['hidden'];
        }
        if (isset($map['labels'])) {
            if (!empty($map['labels'])) {
                $model->labels = $map['labels'];
            }
        }
        if (isset($map['meta'])) {
            $model->meta = $map['meta'];
        }
        if (isset($map['name'])) {
            $model->name = $map['name'];
        }
        if (isset($map['referer'])) {
            $model->referer = $map['referer'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }
        if (isset($map['sign_token'])) {
            $model->signToken = $map['sign_token'];
        }
        if (isset($map['starred'])) {
            $model->starred = $map['starred'];
        }
        if (isset($map['user_meta'])) {
            $model->userMeta = $map['user_meta'];
        }

        return $model;
    }
}
