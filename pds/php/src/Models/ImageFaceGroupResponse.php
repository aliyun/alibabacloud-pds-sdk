<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ImageFaceGroupResponse extends Model
{
    /**
     * @description cover_file_id
     *
     * @var string
     */
    public $coverFileId;

    /**
     * @description 人脸分组生成时间
     *
     * @example 2019-02-20T09:35:51.057Z
     *
     * @var string
     */
    public $createdAt;

    /**
     * @description 人脸个数
     *
     * @example 2
     *
     * @var int
     */
    public $faceCount;

    /**
     * @description 人脸分组封面头像地址
     *
     * @example http://imm-dev-wmt/facegroup/05.jpg?x-oss-process=xxx
     *
     * @var string
     */
    public $groupCoverUrl;

    /**
     * @description 人脸分组 ID
     *
     * @example abc
     *
     * @var string
     */
    public $groupId;

    /**
     * @description 人脸分组名称
     *
     * @example abc
     *
     * @var string
     */
    public $groupName;

    /**
     * @description 照片个数
     *
     * @example 2
     *
     * @var int
     */
    public $imageCount;

    /**
     * @description 人脸分组修改时间
     *
     * @example 2019-02-20T09:35:51.057Z
     *
     * @var string
     */
    public $updatedAt;
    protected $_name = [
        'coverFileId'   => 'cover_file_id',
        'createdAt'     => 'created_at',
        'faceCount'     => 'face_count',
        'groupCoverUrl' => 'group_cover_url',
        'groupId'       => 'group_id',
        'groupName'     => 'group_name',
        'imageCount'    => 'image_count',
        'updatedAt'     => 'updated_at',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->coverFileId) {
            $res['cover_file_id'] = $this->coverFileId;
        }
        if (null !== $this->createdAt) {
            $res['created_at'] = $this->createdAt;
        }
        if (null !== $this->faceCount) {
            $res['face_count'] = $this->faceCount;
        }
        if (null !== $this->groupCoverUrl) {
            $res['group_cover_url'] = $this->groupCoverUrl;
        }
        if (null !== $this->groupId) {
            $res['group_id'] = $this->groupId;
        }
        if (null !== $this->groupName) {
            $res['group_name'] = $this->groupName;
        }
        if (null !== $this->imageCount) {
            $res['image_count'] = $this->imageCount;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ImageFaceGroupResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['cover_file_id'])) {
            $model->coverFileId = $map['cover_file_id'];
        }
        if (isset($map['created_at'])) {
            $model->createdAt = $map['created_at'];
        }
        if (isset($map['face_count'])) {
            $model->faceCount = $map['face_count'];
        }
        if (isset($map['group_cover_url'])) {
            $model->groupCoverUrl = $map['group_cover_url'];
        }
        if (isset($map['group_id'])) {
            $model->groupId = $map['group_id'];
        }
        if (isset($map['group_name'])) {
            $model->groupName = $map['group_name'];
        }
        if (isset($map['image_count'])) {
            $model->imageCount = $map['image_count'];
        }
        if (isset($map['updated_at'])) {
            $model->updatedAt = $map['updated_at'];
        }

        return $model;
    }
}
