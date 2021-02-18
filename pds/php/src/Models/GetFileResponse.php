<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\ImageMediaResponse;
use Aliyun\PDS\SDK\Models\VideoMediaResponse;
use Aliyun\PDS\SDK\Models\VideoPreviewResponse;

/**
 * 获取文件元数据response
 */
class GetFileResponse extends Model {
    protected $_name = [
        'category' => 'category',
        'characteristicHash' => 'characteristic_hash',
        'contentHash' => 'content_hash',
        'contentHashName' => 'content_hash_name',
        'contentType' => 'content_type',
        'crc64Hash' => 'crc64_hash',
        'createdAt' => 'created_at',
        'description' => 'description',
        'domainId' => 'domain_id',
        'downloadUrl' => 'download_url',
        'driveId' => 'drive_id',
        'encryptMode' => 'encrypt_mode',
        'fileExtension' => 'file_extension',
        'fileId' => 'file_id',
        'hidden' => 'hidden',
        'imageMediaMetadata' => 'image_media_metadata',
        'labels' => 'labels',
        'meta' => 'meta',
        'name' => 'name',
        'parentFileId' => 'parent_file_id',
        'punishFlag' => 'punish_flag',
        'shareId' => 'share_id',
        'size' => 'size',
        'starred' => 'starred',
        'status' => 'status',
        'streamsInfo' => 'streams_info',
        'thumbnail' => 'thumbnail',
        'trashedAt' => 'trashed_at',
        'type' => 'type',
        'updatedAt' => 'updated_at',
        'uploadId' => 'upload_id',
        'url' => 'url',
        'userMeta' => 'user_meta',
        'videoMediaMetadata' => 'video_media_metadata',
        'videoPreviewMetadata' => 'video_preview_metadata',
    ];
    public function validate() {
        Model::validatePattern('domainId', $this->domainId, '[a-z0-9A-Z]+');
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9]{1,50}');
        Model::validatePattern('name', $this->name, '[a-zA-Z0-9.-]{1,1000}');
        Model::validatePattern('parentFileId', $this->parentFileId, '[a-z0-9]{1,50}');
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMaxLength('parentFileId', $this->parentFileId, 50);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMinLength('parentFileId', $this->parentFileId, 40);
        Model::validateRequired('name', $this->name, true);
        Model::validateMaximum('size', $this->size, 53687091200);
        Model::validateMinimum('size', $this->size, 0);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->category) {
            $res['category'] = $this->category;
        }
        if (null !== $this->characteristicHash) {
            $res['characteristic_hash'] = $this->characteristicHash;
        }
        if (null !== $this->contentHash) {
            $res['content_hash'] = $this->contentHash;
        }
        if (null !== $this->contentHashName) {
            $res['content_hash_name'] = $this->contentHashName;
        }
        if (null !== $this->contentType) {
            $res['content_type'] = $this->contentType;
        }
        if (null !== $this->crc64Hash) {
            $res['crc64_hash'] = $this->crc64Hash;
        }
        if (null !== $this->createdAt) {
            $res['created_at'] = $this->createdAt;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->downloadUrl) {
            $res['download_url'] = $this->downloadUrl;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->encryptMode) {
            $res['encrypt_mode'] = $this->encryptMode;
        }
        if (null !== $this->fileExtension) {
            $res['file_extension'] = $this->fileExtension;
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
        if (null !== $this->meta) {
            $res['meta'] = $this->meta;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->parentFileId) {
            $res['parent_file_id'] = $this->parentFileId;
        }
        if (null !== $this->punishFlag) {
            $res['punish_flag'] = $this->punishFlag;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->starred) {
            $res['starred'] = $this->starred;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->streamsInfo) {
            $res['streams_info'] = $this->streamsInfo;
        }
        if (null !== $this->thumbnail) {
            $res['thumbnail'] = $this->thumbnail;
        }
        if (null !== $this->trashedAt) {
            $res['trashed_at'] = $this->trashedAt;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }
        if (null !== $this->uploadId) {
            $res['upload_id'] = $this->uploadId;
        }
        if (null !== $this->url) {
            $res['url'] = $this->url;
        }
        if (null !== $this->userMeta) {
            $res['user_meta'] = $this->userMeta;
        }
        if (null !== $this->videoMediaMetadata) {
            $res['video_media_metadata'] = null !== $this->videoMediaMetadata ? $this->videoMediaMetadata->toMap() : null;
        }
        if (null !== $this->videoPreviewMetadata) {
            $res['video_preview_metadata'] = null !== $this->videoPreviewMetadata ? $this->videoPreviewMetadata->toMap() : null;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetFileResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['category'])){
            $model->category = $map['category'];
        }
        if(isset($map['characteristic_hash'])){
            $model->characteristicHash = $map['characteristic_hash'];
        }
        if(isset($map['content_hash'])){
            $model->contentHash = $map['content_hash'];
        }
        if(isset($map['content_hash_name'])){
            $model->contentHashName = $map['content_hash_name'];
        }
        if(isset($map['content_type'])){
            $model->contentType = $map['content_type'];
        }
        if(isset($map['crc64_hash'])){
            $model->crc64Hash = $map['crc64_hash'];
        }
        if(isset($map['created_at'])){
            $model->createdAt = $map['created_at'];
        }
        if(isset($map['description'])){
            $model->description = $map['description'];
        }
        if(isset($map['domain_id'])){
            $model->domainId = $map['domain_id'];
        }
        if(isset($map['download_url'])){
            $model->downloadUrl = $map['download_url'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['encrypt_mode'])){
            $model->encryptMode = $map['encrypt_mode'];
        }
        if(isset($map['file_extension'])){
            $model->fileExtension = $map['file_extension'];
        }
        if(isset($map['file_id'])){
            $model->fileId = $map['file_id'];
        }
        if(isset($map['hidden'])){
            $model->hidden = $map['hidden'];
        }
        if(isset($map['image_media_metadata'])){
            $model->imageMediaMetadata = ImageMediaResponse::fromMap($map['image_media_metadata']);
        }
        if(isset($map['labels'])){
            if(!empty($map['labels'])){
                $model->labels = $map['labels'];
            }
        }
        if(isset($map['meta'])){
            $model->meta = $map['meta'];
        }
        if(isset($map['name'])){
            $model->name = $map['name'];
        }
        if(isset($map['parent_file_id'])){
            $model->parentFileId = $map['parent_file_id'];
        }
        if(isset($map['punish_flag'])){
            $model->punishFlag = $map['punish_flag'];
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['size'])){
            $model->size = $map['size'];
        }
        if(isset($map['starred'])){
            $model->starred = $map['starred'];
        }
        if(isset($map['status'])){
            $model->status = $map['status'];
        }
        if(isset($map['streams_info'])){
            $model->streamsInfo = $map['streams_info'];
        }
        if(isset($map['thumbnail'])){
            $model->thumbnail = $map['thumbnail'];
        }
        if(isset($map['trashed_at'])){
            $model->trashedAt = $map['trashed_at'];
        }
        if(isset($map['type'])){
            $model->type = $map['type'];
        }
        if(isset($map['updated_at'])){
            $model->updatedAt = $map['updated_at'];
        }
        if(isset($map['upload_id'])){
            $model->uploadId = $map['upload_id'];
        }
        if(isset($map['url'])){
            $model->url = $map['url'];
        }
        if(isset($map['user_meta'])){
            $model->userMeta = $map['user_meta'];
        }
        if(isset($map['video_media_metadata'])){
            $model->videoMediaMetadata = VideoMediaResponse::fromMap($map['video_media_metadata']);
        }
        if(isset($map['video_preview_metadata'])){
            $model->videoPreviewMetadata = VideoPreviewResponse::fromMap($map['video_preview_metadata']);
        }
        return $model;
    }
    /**
     * @description category
     * @example doc
     * @var string
     */
    public $category;

    /**
     * @description CharacteristicHash
     * @var string
     */
    public $characteristicHash;

    /**
     * @description Content Hash
     * @example EA4942AA8761213890A5C386F88E6464D2C31CA3
     * @var string
     */
    public $contentHash;

    /**
     * @description content_hash_name
     * @example sha1
     * @var string
     */
    public $contentHashName;

    /**
     * @description content_type
     * @example application/json
     * @var string
     */
    public $contentType;

    /**
     * @description crc64_hash
     * @var string
     */
    public $crc64Hash;

    /**
     * @description created_at
     * @example 2019-08-20T06:51:27.292Z
     * @var string
     */
    public $createdAt;

    /**
     * @description description
     * @example file description
     * @var string
     */
    public $description;

    /**
     * @description DomainID
     * @example test001
     * @var string
     */
    public $domainId;

    /**
     * @description download_url
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $downloadUrl;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description encrypt_mode
     * @example pin
     * @var string
     */
    public $encryptMode;

    /**
     * @description file_extension
     * @example jpg
     * @var string
     */
    public $fileExtension;

    /**
     * @description file_id
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     * @var string
     */
    public $fileId;

    /**
     * @description Hidden
type: boolean
     * @example false
     * @var bool
     */
    public $hidden;

    /**
     * @var ImageMediaResponse
     */
    public $imageMediaMetadata;

    /**
     * @description labels
     * @example label1:1, label2:2
     * @var string[]
     */
    public $labels;

    /**
     * @var string
     */
    public $meta;

    /**
     * @description name
     * @example ccp.jpg
     * @var string
     */
    public $name;

    /**
     * @description parent_file_id
     * @example root
     * @var string
     */
    public $parentFileId;

    /**
     * @var int
     */
    public $punishFlag;

    /**
     * @var string
     */
    public $shareId;

    /**
     * @description Size
     * @example 1024
     * @var int
     */
    public $size;

    /**
     * @description starred
type: boolean
     * @example false
     * @var bool
     */
    public $starred;

    /**
     * @description status
     * @example available
     * @var string
     */
    public $status;

    /**
     * @description @Deprecated streams url info
     * @var mixed[]
     */
    public $streamsInfo;

    /**
     * @description thumbnail
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $thumbnail;

    /**
     * @description trashed_at
     * @var string
     */
    public $trashedAt;

    /**
     * @description type
     * @example file
     * @var string
     */
    public $type;

    /**
     * @description updated_at
     * @var string
     */
    public $updatedAt;

    /**
     * @description upload_id
     * @example C9DCFE5A82644AC7A02DB74C30C934A6
     * @var string
     */
    public $uploadId;

    /**
     * @description url
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d5b986facbec311ef844c25954f96821497b383%2F5d5b986f955410dd991646bb87c6b4e899eff525?Expires=xxx&OSSAccessKeyId=xxx&Signature=xxx
     * @var string
     */
    public $url;

    /**
     * @description user_meta
     * @example user_meta
     * @var string
     */
    public $userMeta;

    /**
     * @var VideoMediaResponse
     */
    public $videoMediaMetadata;

    /**
     * @var VideoPreviewResponse
     */
    public $videoPreviewMetadata;

}
