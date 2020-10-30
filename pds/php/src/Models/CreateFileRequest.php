<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 创建文件.
 */
class CreateFileRequest extends Model
{
    public $headers;

    /**
     * @description addition_data
     *
     * @var mixed[]
     */
    public $additionData;

    /**
     * @var bool
     */
    public $autoRename;

    /**
     * @description check_name_mode
     *
     * @var string
     */
    public $checkNameMode;

    /**
     * @description content_hash
     *
     * @example 7C4A8D09CA3762AF61E59520943DC26494F8941B
     *
     * @var string
     */
    public $contentHash;

    /**
     * @description content_hash_name
     *
     * @example sha1
     *
     * @var string
     */
    public $contentHashName;

    /**
     * @description ContentMd5
     *
     * @example E10ADC3949BA59ABBE56E057F20F883E
     *
     * @var string
     */
    public $contentMd5;

    /**
     * @description ContentType
     *
     * @example application/json
     *
     * @var string
     */
    public $contentType;

    /**
     * @description description
     *
     * @example file description
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
     * @description encrypt_mode
     *
     * @var string
     */
    public $encryptMode;

    /**
     * @description file_id
     *
     * @var string
     */
    public $fileId;

    /**
     * @description hidden
     *
     * @example false
     *
     * @var bool
     */
    public $hidden;

    /**
     * @var ImageMediaMetadata
     */
    public $imageMediaMetadata;

    /**
     * @description labels
     *
     * @example label1, label2
     *
     * @var string[]
     */
    public $labels;

    /**
     * @description last_updated_at
     *
     * @example 2019-08-20T06:51:27.292Z
     *
     * @var string
     */
    public $lastUpdatedAt;

    /**
     * @var string
     */
    public $meta;

    /**
     * @description Name
     *
     * @example ccp.jpg
     *
     * @var string
     */
    public $name;

    /**
     * @description parent_file_id
     *
     * @example root
     *
     * @var string
     */
    public $parentFileId;

    /**
     * @description part_info_list
     *
     * @var UploadPartInfo[]
     */
    public $partInfoList;

    /**
     * @description pre_hash
     *
     * @example E10ADC3949BA59ABBE56E057F20F883E
     *
     * @var string
     */
    public $preHash;

    /**
     * @description Size
     *
     * @var int
     */
    public $size;

    /**
     * @description streams_info
     *
     * @var mixed[]
     */
    public $streamsInfo;

    /**
     * @description Type
     *
     * @example file
     *
     * @var string
     */
    public $type;

    /**
     * @description user_meta
     *
     * @example user_meta
     *
     * @var string
     */
    public $userMeta;

    /**
     * @var VideoMediaMetadata
     */
    public $videoMediaMetadata;
    protected $_name = [
        'additionData'       => 'addition_data',
        'autoRename'         => 'auto_rename',
        'checkNameMode'      => 'check_name_mode',
        'contentHash'        => 'content_hash',
        'contentHashName'    => 'content_hash_name',
        'contentMd5'         => 'content_md5',
        'contentType'        => 'content_type',
        'description'        => 'description',
        'driveId'            => 'drive_id',
        'encryptMode'        => 'encrypt_mode',
        'fileId'             => 'file_id',
        'hidden'             => 'hidden',
        'imageMediaMetadata' => 'image_media_metadata',
        'labels'             => 'labels',
        'lastUpdatedAt'      => 'last_updated_at',
        'meta'               => 'meta',
        'name'               => 'name',
        'parentFileId'       => 'parent_file_id',
        'partInfoList'       => 'part_info_list',
        'preHash'            => 'pre_hash',
        'size'               => 'size',
        'streamsInfo'        => 'streams_info',
        'type'               => 'type',
        'userMeta'           => 'user_meta',
        'videoMediaMetadata' => 'video_media_metadata',
    ];
    protected $_default = [
        'checkNameMode' => 'ignore',
    ];

    public function validate()
    {
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateMaxLength('name', $this->name, 1024);
        Model::validateMaxLength('parentFileId', $this->parentFileId, 50);
        Model::validateMinLength('description', $this->description, 0);
        Model::validateMinLength('name', $this->name, 1);
        Model::validateMinLength('parentFileId', $this->parentFileId, 4);
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('name', $this->name, true);
        Model::validateRequired('parentFileId', $this->parentFileId, true);
        Model::validateRequired('type', $this->type, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('parentFileId', $this->parentFileId, '[a-z0-9]{1,50}');
        Model::validateMaximum('size', $this->size, 53687091200);
        Model::validateMinimum('size', $this->size, 0);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->autoRename) {
            $res['auto_rename'] = $this->autoRename;
        }
        if (null !== $this->checkNameMode) {
            $res['check_name_mode'] = $this->checkNameMode;
        }
        if (null !== $this->contentHash) {
            $res['content_hash'] = $this->contentHash;
        }
        if (null !== $this->contentHashName) {
            $res['content_hash_name'] = $this->contentHashName;
        }
        if (null !== $this->contentMd5) {
            $res['content_md5'] = $this->contentMd5;
        }
        if (null !== $this->contentType) {
            $res['content_type'] = $this->contentType;
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
        if (null !== $this->hidden) {
            $res['hidden'] = $this->hidden;
        }
        if (null !== $this->imageMediaMetadata) {
            $res['image_media_metadata'] = null !== $this->imageMediaMetadata ? $this->imageMediaMetadata->toMap() : null;
        }
        if (null !== $this->labels) {
            $res['labels'] = $this->labels;
        }
        if (null !== $this->lastUpdatedAt) {
            $res['last_updated_at'] = $this->lastUpdatedAt;
        }
        if (null !== $this->meta) {
            $res['meta'] = $this->meta;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->parentFileId) {
            $res['parent_file_id'] = $this->parentFileId;
        }
        if (null !== $this->partInfoList) {
            $res['part_info_list'] = [];
            if (null !== $this->partInfoList && \is_array($this->partInfoList)) {
                $n = 0;
                foreach ($this->partInfoList as $item) {
                    $res['part_info_list'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->preHash) {
            $res['pre_hash'] = $this->preHash;
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->streamsInfo) {
            $res['streams_info'] = $this->streamsInfo;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        if (null !== $this->userMeta) {
            $res['user_meta'] = $this->userMeta;
        }
        if (null !== $this->videoMediaMetadata) {
            $res['video_media_metadata'] = null !== $this->videoMediaMetadata ? $this->videoMediaMetadata->toMap() : null;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateFileRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['addition_data'])) {
            $model->additionData = $map['addition_data'];
        }
        if (isset($map['auto_rename'])) {
            $model->autoRename = $map['auto_rename'];
        }
        if (isset($map['check_name_mode'])) {
            $model->checkNameMode = $map['check_name_mode'];
        }
        if (isset($map['content_hash'])) {
            $model->contentHash = $map['content_hash'];
        }
        if (isset($map['content_hash_name'])) {
            $model->contentHashName = $map['content_hash_name'];
        }
        if (isset($map['content_md5'])) {
            $model->contentMd5 = $map['content_md5'];
        }
        if (isset($map['content_type'])) {
            $model->contentType = $map['content_type'];
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
        if (isset($map['hidden'])) {
            $model->hidden = $map['hidden'];
        }
        if (isset($map['image_media_metadata'])) {
            $model->imageMediaMetadata = ImageMediaMetadata::fromMap($map['image_media_metadata']);
        }
        if (isset($map['labels'])) {
            if (!empty($map['labels'])) {
                $model->labels = $map['labels'];
            }
        }
        if (isset($map['last_updated_at'])) {
            $model->lastUpdatedAt = $map['last_updated_at'];
        }
        if (isset($map['meta'])) {
            $model->meta = $map['meta'];
        }
        if (isset($map['name'])) {
            $model->name = $map['name'];
        }
        if (isset($map['parent_file_id'])) {
            $model->parentFileId = $map['parent_file_id'];
        }
        if (isset($map['part_info_list'])) {
            if (!empty($map['part_info_list'])) {
                $model->partInfoList = [];
                $n                   = 0;
                foreach ($map['part_info_list'] as $item) {
                    $model->partInfoList[$n++] = null !== $item ? UploadPartInfo::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['pre_hash'])) {
            $model->preHash = $map['pre_hash'];
        }
        if (isset($map['size'])) {
            $model->size = $map['size'];
        }
        if (isset($map['streams_info'])) {
            $model->streamsInfo = $map['streams_info'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }
        if (isset($map['user_meta'])) {
            $model->userMeta = $map['user_meta'];
        }
        if (isset($map['video_media_metadata'])) {
            $model->videoMediaMetadata = VideoMediaMetadata::fromMap($map['video_media_metadata']);
        }

        return $model;
    }
}
